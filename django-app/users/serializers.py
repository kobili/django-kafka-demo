from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class UserKafkaSyncSerializer(UserSerializer):
    """
    A serializer that fetches all the data to send to the `user-created` and `user-updated` kafka topics
    """
