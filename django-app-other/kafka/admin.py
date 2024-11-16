from django.contrib import admin

from kafka.models import KafkaProducerLog, KafkaConsumerLog

@admin.register(KafkaProducerLog)
class KafkaProducerLogAdmin(admin.ModelAdmin):
    list_display = ["topic", "key", "is_success", "partition", "offset"]


@admin.register(KafkaConsumerLog)
class KafkaConsumerLogAdmin(admin.ModelAdmin):
    list_display = ["event_topic", "event_key", "is_success"]
