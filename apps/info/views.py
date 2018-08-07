from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
import json
from django.contrib.auth import get_user_model

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from rest_framework import permissions, authentication
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.authentication import SessionAuthentication

from .models import RobotInfo
from .serializers import RobotCreateSerializer, RobotDetailSerializer

User = get_user_model()


class RobotInfoViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Robot Info
    """
    # a view set must set the serializer class info
    serializer_class = RobotCreateSerializer
    queryset = RobotInfo.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        """
        get the current serializer class
        :return: Current Serializer
        """
        if self.action == "create":
            return RobotCreateSerializer
        return RobotDetailSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=serializer)
        re_dict = serializer.data
        # rewrite the robot create user
        re_dict["user"] = self.request.user.username if self.request.user else "robot"
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
