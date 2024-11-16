from rest_framework import routers

from users.views import ExternalUserViewSet


router = routers.DefaultRouter()

router.register(r"external_users", ExternalUserViewSet)

urlpatterns = router.urls
