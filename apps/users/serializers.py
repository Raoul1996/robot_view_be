from rest_framework import serializers

from .models import UserProfile, EmailVerifyRecord


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('nick_name', 'gender', 'mobile', 'email', 'image')
