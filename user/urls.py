from django.urls import include, path
from rest_framework import routers

from .views import RegisterView, RegisterAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path("", include(router.urls))
]

urlpatterns += router.urls