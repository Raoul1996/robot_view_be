from django.shortcuts import render
from django_thrift.handler import create_handler

handler = create_handler()


@handler.map_function("saveRobotData")
def save_robot_data_handler():
    return {"a": "bb"}


@handler.map_function("ping")
def ping_handler():
    return "pong"


@handler.map_function("say")
def say_handler(msg):
    res = "Received: " + msg
    print(res)
    return res
