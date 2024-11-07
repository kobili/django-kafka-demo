from confluent_kafka import Producer

producer = Producer({
    "bootstrap.servers": "kafka:9092", # TODO: move to ENV

    "acks": "all",
})

def kafka_delivery_callback(err, msg):
    if err:
        print("ERROR: Event failed delivery: {}".format(err))
    else:
        print("Produced event to topic {topic}: {value}".format(topic=msg.topic(), value=msg.value().decode("utf-8")))

KAFKA_TOPIC_USER_CREATED = "user-created"
KAFKA_TOPIC_USER_UPDATED = "user-updated"
