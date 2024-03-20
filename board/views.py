from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import status

from .serializers import BoardSerializer
from .models import Board
from .permissions import UpdateOwnProfile


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


class BoardApiView(APIView):
    authentication_classes = (JWTAuthentication, )

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

    def get(self, request):
        # query, serializer를 구현해 주어야 한다.
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


