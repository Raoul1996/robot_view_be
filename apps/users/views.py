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
from utils.yunpian import YunPian
from robot_view.settings import API_KEY

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    custom user validate rules
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
    send SMS Code
    """
    serializer_class = SMSSerializer

    @staticmethod
    def generate_code():
        """
        generate a verify string which include 4 number
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
        yun_pian = YunPian(API_KEY)
        code = self.generate_code()
        sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        # example sms_status = {'code': 0, 'msg': 'hello'}
        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({"mobile": mobile}, status=status.HTTP_201_CREATED)


class UserViewSets(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    User ViewSet
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def get_serializer_class(self):
        """
        get the current serializer class,
        if the action type is create, return the register serializer
        """
        if self.action == "create":
            return UserRegSerializer
        return UserDetailSerializer

    def get_permissions(self):
        """
        only the user who is authenticated can retrieve the user's detail.
        """
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return []

    def create(self, request, *args, **kwargs):
        """
        rewrite the create function
        :param request:
        :param args:
        :param kwargs:
        :return: Response:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer=serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        """
        rewrite this function, only return the current user who send the request
        """
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()
