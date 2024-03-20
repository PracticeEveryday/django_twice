from rest_framework.permissions import AllowAny
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

    def get(self, request):
        # query, serializer를 구현해 주어야 한다.
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


