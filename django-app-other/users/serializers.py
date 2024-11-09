from rest_framework import serializers

from users.models import ExternalUser


class ExternalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalUser
        fields = [
            "id",
            "source_id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]
