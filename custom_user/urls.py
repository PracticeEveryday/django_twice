from django.urls import include, path

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path("auth/", AuthAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("", include(router.urls))
]

urlpatterns += router.urls