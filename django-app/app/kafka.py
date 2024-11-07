import json
from confluent_kafka import Producer

# TODO: Move this stuff into a separa "kafka" app

def _kafka_delivery_callback(err, msg):
    # TODO: make this create an audit log or something
    if err:
        print("ERROR: Event failed delivery: {}".format(err))
    else:
        print("Produced event to topic {topic}: {value}".format(topic=msg.topic(), value=msg.value().decode("utf-8")))


KAFKA_TOPIC_USER_CREATED = "user-created"
KAFKA_TOPIC_USER_UPDATED = "user-updated"


class KafkaProducer:
    def __init__(self, kafka_config: dict):
        self.producer = Producer(kafka_config)

    def produce(self, topic: str, value: dict | str, key: str=None) -> None:
        if isinstance(value, dict):
            value = json.dumps(value)

        self.producer.produce(topic, value=value, key=key, callback=_kafka_delivery_callback)
        self.producer.poll(10)
        self.producer.flush()


producer = KafkaProducer({
    "bootstrap.servers": "kafka:9092", # TODO: move to ENV
    "acks": "all",
})
