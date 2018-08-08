import json
from django_thrift.handler import create_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from .models import RobotData
from .serializers import RobotDataSerializer

handler = create_handler()


class RobotDataViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """
    Robot Data
    """
    serializer_class = RobotDataSerializer
    queryset = RobotData.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


@handler.map_function("RobotInfo")
def robot_info_handler(robot_name, info):
    """

    :param robot_name: robot name, unique value
    :param info: robot upload information
    :return: return string map
    """
    try:
        RobotData.objects.create(name=robot_name, data=info)
        return {0: 'ok'}
    except Exception as e:
        return {-1: json.dumps(e)}


@handler.map_function("saveRobotData")
def save_robot_data_handler():
    return {"a": "bb"}


@handler.map_function("ping")
def ping_handler():
    return "pong"


@handler.map_function("say")
def say_handler(msg):
    print(json.loads(msg))
    res = "Received: " + msg
    print(res)
    return res
