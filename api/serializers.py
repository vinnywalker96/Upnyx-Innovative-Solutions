from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from .models import User, Chat
from django.utils import timezone
from django.conf import settings

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if not data.get('username'):
            raise serializers.ValidationError("Username is required")

        if not data.get('password'):
            raise serializers.ValidationError("Password is required")

        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, min_length=8)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid username or password, try again')

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'tokens']


class ChatSerializer(serializers.ModelSerializer):
    message = serializers.CharField()
    class Meta:
        model = Chat
        fields = ['id', 'user', 'message', 'response', 'timestamp']
        read_only_fields = ['id','user', 'response', 'timestamp']
