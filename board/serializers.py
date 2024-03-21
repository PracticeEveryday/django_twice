from rest_framework import serializers

from .models import *


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'content']

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "content": instance.content,
            "create_ts": instance.create_ts
        }