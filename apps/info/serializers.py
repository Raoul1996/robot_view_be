from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import RobotInfo

User = get_user_model()


class RobotCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True,
                                 label='robot_name',
                                 allow_blank=False,
                                 validators=[UniqueValidator(
                                     queryset=RobotInfo.objects.all(),
                                     message="robot is already exist."
                                 )])

    class Meta:
        model = RobotInfo
        fields = ['name', 'type', 'user']


class RobotDetailSerializer(serializers.ModelSerializer):
    """
    Robot Detail Serializer
    """

    class Meta:
        model = RobotInfo
        fields = "__all__"
