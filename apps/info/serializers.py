from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import RobotInfo

User = get_user_model()


class RobotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotInfo
        fields = ['name', 'type']


class RobotDetailSerializer(serializers.ModelSerializer):
    """
    Robot Detail Serializer
    """

    class Meta:
        model = RobotInfo
        fields = "__all__"
