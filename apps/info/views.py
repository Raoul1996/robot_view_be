from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication

from .models import RobotInfo
from .serializers import RobotCreateSerializer, RobotDetailSerializer

User = get_user_model()


class RobotInfoViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
    Robot Info
    """
    # a view set must set the serializer class info
    serializer_class = RobotCreateSerializer
    queryset = RobotInfo.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        """
        get the current serializer class
        :return: Current Serializer
        """
        if self.action == "create":
            return RobotCreateSerializer
        return RobotDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=serializer)
        robot = self.perform_create(serializer=serializer)
        re_dict = serializer.data
        # rewrite the robot create user
        if robot.user.username:
            re_dict["user"] = robot.user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        re_dict = serializer.data
        re_dict["user"] = User.objects.get(Q(id=re_dict["user"])).username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_200_OK, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
