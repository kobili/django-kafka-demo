from django.conf import settings

from kafka.client import KafkaProducer


producer = KafkaProducer({
    "bootstrap.servers": settings.KAFKA_BOOTSTRAP_SERVERS,
    "acks": "all",
})
