import json
from django.db import models

from app.kafka import producer, KAFKA_TOPIC_USER_CREATED, KAFKA_TOPIC_USER_UPDATED, kafka_delivery_callback

# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True)
    email = models.CharField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()

    def save(self, *args, **kwargs):
        from users.serializers import UserKafkaSyncSerializer

        creating = self._state.adding
        super().save(*args, **kwargs)

        kafka_event = json.dumps(UserKafkaSyncSerializer(instance=self).data)
        kafka_topic = KAFKA_TOPIC_USER_CREATED if creating else KAFKA_TOPIC_USER_UPDATED

        producer.produce(kafka_topic, value=kafka_event, callback=kafka_delivery_callback)
        producer.poll(1)
        producer.flush()

        return
