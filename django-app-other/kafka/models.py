from django.db import models
from django.utils import timezone


class KafkaProducerLog(models.Model):
    topic = models.CharField(max_length=100, db_index=True)
    key = models.CharField(max_length=100, null=True, blank=True)
    value = models.TextField()
    partition = models.CharField(max_length=50, null=True, blank=True)
    offset = models.CharField(max_length=50, null=True, blank=True)

    is_success = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Kafka Producer Log"
        verbose_name_plural = "Kafka Producer Logs"


class KafkaConsumerLog(models.Model):
    event_topic = models.CharField(max_length=100, db_index=True)
    event_key = models.CharField(max_length=100, null=True, blank=True)
    event_value = models.TextField()
    consumer_group_id = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text="The consumer group that handled the event.",
    )

    is_success = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Kafka Consumer Log"
        verbose_name_plural = "Kafka Consumer Logs"
