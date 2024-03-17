from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser

    def create_manager(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = False
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class CustomUser(AbstractBaseUser, PermissionsMixin):
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

    # 헬퍼 클래스 사용
    objects = CustomUserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email
