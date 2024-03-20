
from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

    # 반환 값 Serialization
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
        }
