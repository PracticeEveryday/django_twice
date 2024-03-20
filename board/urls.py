from django.urls import include, path
from rest_framework import routers
from .views import BoardViewSet, BoardApiView

router = routers.DefaultRouter()
router.register(r'viewsets', BoardViewSet, basename='board')

urlpatterns = [
    path("api_view/", BoardApiView.as_view()),
    path("", include(router.urls))
]

urlpatterns += router.urls
