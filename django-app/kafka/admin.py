from django.contrib import admin

from kafka.models import KafkaProducerLog

@admin.register(KafkaProducerLog)
class KafkaProducerLogAdmin(admin.ModelAdmin):
    list_display = ["topic", "key", "is_success", "partition", "offset"]
