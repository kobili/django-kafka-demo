import signal

from django.core.management.base import BaseCommand
from django.conf import settings

from confluent_kafka import Consumer, KafkaError, KafkaException
from users.constants import KAFKA_TOPIC_USER_UPDATED


class Command(BaseCommand):
    help = "Initializes and starts a long running Kafka consumer to sync user data from an external source"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        signal.signal(signal.SIGINT, self.terminate)
        signal.signal(signal.SIGTERM, self.terminate)

        self.running = True

    def handle(self, *args, **options):
        # start kafka consumer
        consumer = Consumer({
            "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS,
            "group.id": "foo-consumer",
            "auto.offset.reset": "earliest",
            'enable.auto.commit': "true",
            'enable.auto.offset.store': "false",
        })

        try:
            consumer.subscribe([KAFKA_TOPIC_USER_UPDATED])

            while self.running:
                msg = consumer.poll(timeout=1.0)

                if msg is None:
                    # Continue polling if there are no messages
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError.__PARTITION_EOF:
                        print("No messages in partition")
                    else:
                        raise KafkaException(msg.error())
                
                else:
                    # Create/update users
                    print({
                        "topic": msg.topic(),
                        "key": msg.key().decode("utf-8"),
                        "value": msg.value().decode("utf-8"),
                    })

        finally:
            # TODO: Perform shutdown events here; cleanup kafka client; commit kafka consumer offsets
            print("closing consumer")
            consumer.close()

            print("done!")

    def terminate(self, signum, frame):
        print(f"received signal: {signum}")
        self.running = False

