from rest_framework import viewsets

from users.models import ExternalUser
from users.serializers import ExternalUserSerializer


class ExternalUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalUser.objects.all()
    serializer_class = ExternalUserSerializer
