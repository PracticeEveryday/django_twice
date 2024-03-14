from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
# router.register(r'groups' GroupViewS)


urlpatterns = [
    path("", include(router.urls)),
    # path('api-auth/', include("rest_framework.urls", namespace='rest_framework'))
]

urlpatterns += router.urls