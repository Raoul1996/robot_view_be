# robot_view_be

> robot attachment viewer backend

[![Build Status](https://travis-ci.org/Raoul1996/robot_view_be.svg?branch=master)](https://travis-ci.org/Raoul1996/robot_view_be)

### Install

```py
pip3 install -r ./requirement.txt
```
### Run in development env

```py
python3 manage.py runserver --settings=robot_view.dev_settings
```
or

```py
./dev_robot.sh
```
### Run in Production env

Please install the docker-compose before your use it.

```py
docker-compose build && docker-compose up
```
then visit the [localhost:8000](http://localhost:8000)

### Info
1. [deployment via docker, nginx and uwsgi](https://github.com/yiyuhao/SanHui/tree/master/docker)