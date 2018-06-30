from rest_framework import serializers

from .models import UserProfile, EmailVerifyRecord


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'nick_name', 'username', 'gender', 'mobile', 'email', 'image')


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifyRecord
        field = ('code', 'email')
