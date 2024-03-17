from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import BoardSerializer
from .models import Board
from .permissions import UpdateOwnProfile


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (UpdateOwnProfile, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

