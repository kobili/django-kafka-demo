from kafka.client import KafkaProducer


producer = KafkaProducer({
    "bootstrap.servers": "kafka:9092", # TODO: move to ENV
    "acks": "all",
})
