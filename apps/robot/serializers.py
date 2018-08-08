from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import RobotData

User = get_user_model()


class RobotDataSerializer(ModelSerializer):
    class Meta:
        model = RobotData
        fields = "__all__"
