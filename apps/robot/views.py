import json
from django.shortcuts import render
from django_thrift.handler import create_handler

handler = create_handler()


@handler.map_function("RobotInfo")
def robot_info_handler(robot_id, info):
    print(robot_id, info)
    return {0: 'ok'}


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
