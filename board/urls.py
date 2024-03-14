from django.urls import include, path
from rest_framework import routers
from .views import BoardViewSet

router = routers.DefaultRouter()
router.register(r'', BoardViewSet, basename='board')

urlpatterns = [
    path("", include(router.urls))
]

# urlpatterns += router.urls
