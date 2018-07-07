import re
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from robot_view.settings import REGEX_MOBILE
from .models import VerifyCode

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化
    """

    class Meta:
        model = User
        field = ("username", "gender", "email", "mobile")


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, error_messages={
        "blank": "code is not exist",
        "required": "code is not exist",
        "max_length": "code format is illegal.",
        "min_length": "code format is illegal."
    }, help_text="verify_code")
    username = serializers.CharField(required=True,
                                     label="username",
                                     help_text="username",
                                     allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message="user is already exist.")])
    password = serializers.CharField(style={'input_type': 'password'},
                                     help_text="password",
                                     label="password",
                                     write_only=True)

    def validate_code(self, code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]

            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minute_ago > last_record.add_time:
                raise serializers.ValidationError("verify_code is expired.")
            if last_record.code != code:
                raise serializers.ValidationError("verify_code is illegal.")
        else:
            raise serializers.ValidationError("verify_code is illegal.")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        field = ("username", "code", "mobile", "password")


class SMSSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(max_length=11)

    @staticmethod
    def validate_mobile(mobile):
        """
        验证手机号码（函数名称必须是 validate_+ 字段名）
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("User already exist.")

        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("Mobile is not current.")

        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)

        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("please send SMS later.")
        return mobile
