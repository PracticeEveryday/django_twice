from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **kwargs):
#         if not email:
#             return ValueError("Email 필드는 필수입니다.")
#
#         user = self.model(
#             email=email
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         superuser = self.create_user(email=email, password=password)
#
#         superuser.is_staff = True
#         superuser.is_superuser = True
#         superuser.is_active = True
#
#         superuser.save(using=self._db)
#
#         return superuser
#
#     def create_manager(self, email=None, password=None, **extra_fields):
#         manager = self.create_user(email=email, password=password)
#
#         manager.is_staff = True
#         manager.is_superuser = False
#         manager.is_active = True
#
#         manager.save(using=self._db)
#
#         return manager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # nullable False, Blank False <- 빈 값도 안됩니다.
    email = models.EmailField(
        'Email',
        max_length=60,
        unique=True,
        null=False,
        blank=False,
        help_text='Email Field'
    )
    is_superuser = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        help_text='superuser 여부입니다.'
   )
    is_active = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        help_text='활성화 상태 여부입니다.'
    )
    is_staff = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        help_text='Staff 여부입니다.'
    )
    created_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now_add=True,
        help_text='생성된 날짜입니다.'
    )
    updated_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now=True,
        help_text='업데이트 된 날짜입니다.'
    )

    USERNAME_FIELD = 'email',  # 사용자의 username을 email로 설정합니다. <- 이메일로 로그인합니다.
    # objects = CustomUserManager(),

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email


