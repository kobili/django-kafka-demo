from django.contrib import admin

from users.models import ExternalUser

@admin.register(ExternalUser)
class ExternalUserAdmin(admin.ModelAdmin):
    list_display = ["source_id", "username", "email"]
