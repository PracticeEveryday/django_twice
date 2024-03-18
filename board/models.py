from django.db import models
from custom_user.models import CustomUser


class Board(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text='CustomUser Foreign Key'

    )
    title = models.CharField(max_length=50, help_text='Board 제목')
    content = models.CharField(max_length=255, help_text='Board 컨텐츠')
    create_ts = models.DateTimeField(auto_now_add=True, help_text='생성 시간')
    update_ts = models.DateTimeField(auto_now=True, help_text='수정 시간')

    def __str__(self):
        return self.title
