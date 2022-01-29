from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import MMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MessageSerializer(serializers.ModelSerializer):
    user_from = UserSerializer(many=False, read_only=True)
    user_to = UserSerializer(many=False, read_only=True)

    class Meta:
        model = MMessage
        fields = ('id', 'user_from', 'user_to', 'title', 'body', 'sent')


class NewMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MMessage
        fields = ('id', 'user_from', 'user_to', 'title', 'body')




