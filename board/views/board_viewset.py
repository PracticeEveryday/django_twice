from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from board.models import Board
from board.permissions import UpdateOwnProfile
from board.serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (UpdateOwnProfile, )
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
