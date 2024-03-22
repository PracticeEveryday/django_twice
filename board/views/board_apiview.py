from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from board.models import Board
from board.serializers import BoardSerializer


class BoardApiView(APIView):
    authentication_classes = (JWTAuthentication, )

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]

    def get(self, request):
        # query, serializer를 구현해 주어야 한다.
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetailApiView(APIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, pk=None):
        if pk is not None:
            try:
                board = Board.objects.get(pk=pk)
            except Board.DoesNotExist:
                return Response({"message": "게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)




