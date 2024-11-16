from django.db import models


class ExternalUser(models.Model):
    source_id = models.BigIntegerField(unique=True)

    username = models.CharField(unique=True)
    email = models.CharField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
