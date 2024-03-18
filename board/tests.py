from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from custom_user.models import CustomUser
from .models import Board

class BoardApiTest(TestCase):
    # 테스트 코드가 실행되기 전에 호출됩니다.
    def setUp(self):
        # API 요청을 할 수 있도록 도와주는 클라이언트 생성
        self.client = APIClient()
        # User 생성 및 인증 사용자 지정
        self.user = CustomUser.objects.create_user(email="test123@test.com", password="test12345")
        self.client.force_authenticate(user=self.user)

    def test_create_board(self):
        url = "/board/"
        data = {'title': "BOARD TEST TITLE", 'content': "BOARD CONTENT"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(Board.objects.get().title, 'BOARD TEST TITLE')
        self.assertEqual(Board.objects.get().content, 'BOARD CONTENT')