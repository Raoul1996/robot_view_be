from rest_framework import serializers

from .models import User, EmailVerifyRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nick_name', 'username', 'gender', 'mobile', 'email', 'image')


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifyRecord
        field = ('code', 'email')
