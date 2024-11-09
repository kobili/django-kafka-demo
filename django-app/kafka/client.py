import json

from confluent_kafka import Producer

from kafka.models import KafkaProducerLog


def _create_delivery_log(err, msg):
    producer_log_kwargs = {
        "topic": msg.topic(),
        "key": msg.key().decode("utf-8"),
        "value": msg.value().decode("utf-8"),
    }

    if err:
        producer_log_kwargs["error_message"] = f"ERROR: Event failed delivery: {err}"
        producer_log_kwargs["is_success"] = False
    else:
        producer_log_kwargs["partition"] = msg.partition()
        producer_log_kwargs["offset"] = msg.offset()

    KafkaProducerLog.objects.create(**producer_log_kwargs)


class KafkaProducer:
    def __init__(self, kafka_config: dict):
        self.producer = Producer(kafka_config)

    def produce(self, topic: str, key: str, value: dict | str):
        if isinstance(value, dict):
            value = json.dumps(value)

        self.producer.produce(topic, value=value, key=key, callback=_create_delivery_log)
        self.producer.poll(10)

        # TODO: see if there's a better way to do this; ie: we shouldn't be flushing on every event published
        self.producer.flush()
