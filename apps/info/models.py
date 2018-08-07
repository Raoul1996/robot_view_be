from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RobotInfo(models.Model):
    ROBOT_TYPE = (
        ("car", "car"),
        ("plane", "plane")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    name = models.CharField(max_length=255, verbose_name="robot_name", unique=True)
    type = models.CharField(max_length=100, choices=ROBOT_TYPE, verbose_name="robot_type", default="car")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'robot_info'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
