from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RobotData(models.Model):
    name = models.CharField(max_length=100, verbose_name="robot_name", null=False, blank=False,
                            help_text="robot unique name")
    data = models.TextField(verbose_name="robot_data", null=False, blank=False,
                            help_text="robot data json data")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time", help_text="add time")

    class Meta:
        verbose_name = 'robot_data'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
