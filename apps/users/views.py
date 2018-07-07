from random import choice

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins, permissions, authentication
from rest_framework import viewsets, status
from .models import VerifyCode
from .serializers import SMSSerializer, UserDetailSerializer, UserRegSerializer

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SMSCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """

    @staticmethod
    def generate_code():
        """
        生成四位数字的验证码字符串
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        # yun_pian = YunPian(APIKEY)
        code = self.generate_code()
        # sms_status = yun_pian.send_sms(code=code,mobile=mobile)
        sms_status = {'code': 0, 'msg': 'hello'}
        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({"mobile": mobile}, status=status.HTTP_201_CREATED)
