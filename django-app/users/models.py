import json
from django.db import models

from app.kafka import producer, KAFKA_TOPIC_USER_UPDATED

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

        kafka_event = UserKafkaSyncSerializer(instance=self).data
        kafka_event["creating"] = creating

        producer.produce(
            KAFKA_TOPIC_USER_UPDATED,
            value=json.dumps(kafka_event),
        )
