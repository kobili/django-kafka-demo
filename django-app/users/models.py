import json
from django.db import models

from users.constants import KAFKA_TOPIC_USER_UPDATED
from app.kafka import producer


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
            key=str(self.id),
            value=json.dumps(kafka_event),
        )
