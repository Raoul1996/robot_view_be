# encoding: utf-8
from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女"),
    )
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=u"性别", default="female")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"电话")
    email = models.CharField(max_length=50, verbose_name=u"邮箱")
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name=u"头像")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码"),
        ("update_email", u"修改邮箱")
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置 null = true, blank = true 默认不为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.code, self.email)
