import signal
import json

from django.core.management.base import BaseCommand
from django.conf import settings

from confluent_kafka import Consumer, KafkaError, KafkaException
from users.constants import KAFKA_TOPIC_USER_UPDATED
from users.models import ExternalUser
from kafka.models import KafkaConsumerLog


class Command(BaseCommand):
    help = "Initializes and starts a long running Kafka consumer to sync user data from an external source"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        signal.signal(signal.SIGINT, self.terminate)
        signal.signal(signal.SIGTERM, self.terminate)

        self._consumer_group_id = "django-other-user-consumer"

        self.consumer = Consumer({
            "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS,
            "group.id": self._consumer_group_id,
            "auto.offset.reset": "earliest",
            'enable.auto.commit': "true",
            "auto.commit.interval.ms": 5000,
            'enable.auto.offset.store': "false",
        })

        self.running = True

    def handle(self, *args, **options):
        try:
            print(f"Consumer Group ID: {self._consumer_group_id}")

            topics = [KAFKA_TOPIC_USER_UPDATED]
            self.consumer.subscribe(topics)
            print(f"subscribed to topics: {topics}")

            while self.running:
                msg = self.consumer.poll(timeout=1.0)

                if msg is None:
                    # Continue polling if there are no messages
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print("No messages in partition")
                    else:
                        raise KafkaException(msg.error())
                
                else:
                    self.process_user_event(msg)
                    self.consumer.store_offsets(msg)

        finally:
            print("closing consumer")
            self.consumer.close()

            print("done!")

    def terminate(self, signum, frame):
        print(f"received signal: {signum}")
        self.running = False

    def process_user_event(self, msg):
        event = {
            "event_topic": msg.topic(),
            "event_key": msg.key().decode("utf-8"),
            "event_value": msg.value().decode("utf-8"),
        }
        print(f"processing event: {event}")
        consumption_log = KafkaConsumerLog(consumer_group_id=self._consumer_group_id, **event)

        try:
            payload = json.loads(msg.value().decode("utf-8"))

            external_id = payload.pop("id")

            ExternalUser.objects.update_or_create(source_id=external_id, defaults=payload)
        except Exception as e:
            consumption_log.error_message = str(e)
            consumption_log.is_success = False
        
        finally:
            consumption_log.save()

