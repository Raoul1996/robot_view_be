from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RobotData(models.Model):
    robot_id = models.IntegerField(verbose_name="robot_id", null=False, blank=False),
    data = models.TextField(verbose_name="robot_data", null=False, blank=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'robot_data'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.add_time
