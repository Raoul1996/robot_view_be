from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户表，新增字段
    """
    GENDER_CHOICES = (
        ("male", "male"), ("female", "female")
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female", verbose_name="gender",
                              help_text="user's gender, only can select 'male' or 'female' ")
    mobile = models.CharField(max_length=100, null=True, blank=True, verbose_name="mobile",
                              help_text="mobile number, usually contain 11 number, like '15033517890'")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="email",
                              help_text="email address, like 'neuq@neuq.edu.cn'")

    class Meta:
        verbose_name = "user_profile",
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码，回填验证码进行验证。可以保存在 redis 中
    """
    code = models.CharField(max_length=10, verbose_name="verify_code",
                            help_text="verify code, contain 4 numbers. in development env, the value is 1234")
    mobile = models.CharField(max_length=11, verbose_name="mobile",
                              help_text="mobile number, usually contain 11 number, like '15033517890'")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time", help_text="add item time")

    class Meta:
        verbose_name = "SMS_verify"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
