from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from custom_user.models import CustomUser
from .models import Board
from .permissions import UpdateOwnProfile


class BoardApiTest(TestCase):
    # 테스트 코드가 실행되기 전에 호출됩니다.
    def setUp(self):
        # API 요청을 할 수 있도록 도와주는 클라이언트 생성
        self.client = APIClient()
        # User 생성 및 인증 사용자 지정
        self.user = CustomUser.objects.create_user(email="test@test.com", password="test12345")

        # header에 토큰 추가
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        Board.objects.create(title="Sample Title", content="Sample Content", user=self.user)

    def test_viewsets_create_board(self):
        url = "/board/viewsets/"
        data = {'title': "BOARD TEST TITLE", 'content': "BOARD CONTENT"}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 2)
        self.assertEqual(Board.objects.last().title, 'BOARD TEST TITLE')
        self.assertEqual(Board.objects.last().content, 'BOARD CONTENT')
        self.assertEqual(Board.objects.last().id, 2)

    def test_get_board(self):
        url = "/board/api_view/"
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Board.objects.count(), 1)

