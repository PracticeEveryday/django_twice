from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPIView, UserLoginApiView


router = routers.DefaultRouter()

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('login/', UserLoginApiView.as_view()),
    path("", include(router.urls))
]

urlpatterns += router.urls