from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户表，新增字段
    """
    GENDER_CHOICES = (
        ("mail", "mail"), ("female", "female")
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="name")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female", verbose_name="gender")
    mobile = models.CharField(max_length=100, null=True, blank=True, verbose_name="phone", help_text="phone")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="email")

    class Meta:
        verbose_name = "user_profile",
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码，回填验证码进行验证。可以保存在 redis 中
    """
    code = models.CharField(max_length=10, verbose_name="verify_code")
    mobile = models.CharField(max_length=11, verbose_name="phone")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "SMS_verify"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
