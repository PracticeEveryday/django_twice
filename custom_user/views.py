import jwt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from django.conf import settings


from .serializers import *
from .models import CustomUser


class AuthAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        elif self.request.method == 'GET':
            return [IsAuthenticated()]

    @staticmethod
    def get(request):
        try:
            bearer = request.headers['Authorization']
            access_token = bearer.split(" ")[1]
            decoded = jwt.decode(access_token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
            pk = decoded.get('user_id')
            user = get_object_or_404(CustomUser, pk=pk)
            serializer = UserSerializer(instance=user)
            res = Response(serializer.data, status=status.HTTP_200_OK)

            return res

        except jwt.exceptions.ExpiredSignatureError:
            data = {'refresh': request.COOKIES.get('refresh', None)}
            serializer = TokenRefreshSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get('access', None)
                refresh = serializer.data.get('refresh', None)
                payload = jwt.decode(access, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(CustomUser, pk=pk)
                serializer = UserSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie('refresh', refresh)
            else:
                raise jwt.exceptions.InvalidTokenError

        except jwt.exceptions.InvalidTokenError:
            return Response('Invalid Token', status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(self, request):
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )

        if user is not None:
            serializer = UserSerializer(user)

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # create 메소드를 호출한다.
            user = serializer.save()

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            # Refresh Token 토큰 => 쿠키에 저장
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



