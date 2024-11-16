from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import ExternalUser
from users.serializers import ExternalUserSerializer


class ExternalUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExternalUser.objects.all()
    serializer_class = ExternalUserSerializer

    @action(methods=["POST"], detail=False)
    def kafka_sync(self, *args, **kwargs):
        # TODO: add kafka consumers here
        return Response({"message": "would have run kafka consumers"}, status=status.HTTP_200_OK)
