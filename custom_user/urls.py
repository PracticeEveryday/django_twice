from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()), # jwt 토큰 재발급
    path("register/", RegisterAPIView.as_view()),
    path("", include(router.urls))
]

urlpatterns += router.urls