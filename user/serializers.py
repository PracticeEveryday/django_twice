from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    #
    # username = serializers.CharField(
    #     required=True,
    #     max_length=50
    # )
    #
    # password = serializers.CharField(
    #     write_only=True,
    #     required=True,
    #     validators=[validate_password]
    # )


    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email']
    #     )
    #
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     token = Token.objects.create(user=user)
    #
    #     return user
