from rest_framework import serializers
from . import models

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'body', 'user', 'created_at')