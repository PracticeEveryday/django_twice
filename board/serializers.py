from rest_framework import serializers

from .models import *


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'content']