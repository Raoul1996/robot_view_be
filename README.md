# robot_view_be

> robot attachment viewer backend

[![Build Status](https://travis-ci.org/Raoul1996/robot_view_be.svg?branch=prod)](https://travis-ci.org/Raoul1996/robot_view_be)
[![CircleCI](https://circleci.com/gh/Raoul1996/robot_view_be/tree/dev.svg?style=svg)](https://circleci.com/gh/Raoul1996/robot_view_be/tree/dev)
## Run in development env

## Run in development env

### Install

```py
pip3 install -r ./requirement.txt
```
### Run

```py
python3 manage.py runserver --settings=robot_view.dev_settings
```
or

```py
./dev_robot.sh
```
## Run in Production env

Please install the docker-compose before you use it.

```py
docker-compose build && docker-compose up
```
then visit the [localhost:8000](http://localhost:8000)

## Resource
1. [deployment via docker, nginx and uwsgi](https://github.com/yiyuhao/SanHui/tree/master/docker)
2. [使用 CircleCI 实现持续集成和持续部署](https://ruiming.me/continuous-integration-and-deployment/)
## Note

### add a [README.md] to typing your note and problem

### use docker in production env
use docker can make deploy more easy than before, and use the same system env can solve the cross-platform problems

1. create the [Dockerfile](Dockerfile) file
2. Install the `docker-compose` command tools and create the [docker-compose.yml](docker-compose.yml) file
3. run `docker-compose build` to build the web image and database image, use `docker-compose run` to run these containers

### use travis-ci to deploy the application automatic
1. login travis-ci and add the current repos on github
2. create the [`.travis.yml`](.travis.yml) in project
3. add the ssh key by this command, in order to deploy the code to server

```shell
travis encrypt-file ~/.ssh/id_rsa --add
```
### split the settings file for dev env and production env

because I prefer using mysql database in the dev env, and use postgres in production env in docker container, so split the settings is very important.
there are many blog can search form google, just use the simplest method.

1. create the [`dev_settings.py`](robot_view/dev_settings.py)
2. import all item in [`settings.py`](robot_view/settings.py)
3. overwrite the item what you want to change.
4. run commands in [`manage.py`](manage.py) with `--settings=robot_view.dev_settings` or other settings file, default setting file is `settings.py` in `robot_view`

### move app to apps path
if app has very huge number, leave them in the project root path is not a smart choice, so create the `apps` path to store them

1. modify the [`settings.py`](robot_view/settings.py), to configure the apps as resource path

```py
+ import os
  import sys

  # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
+  sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```
2. if use pycharm, also can mark the `apps` path as `Source Root`, trust me, It's a smart action.

### change pip registry to douban

```shell
pip3 install -r /code/robot/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```
if use docker, modify the [Dockerfile](Dockerfile)

```Dockerfile
- RUN pip3 install -r /code/robot/requirements.txt
+ RUN pip3 install -r /code/robot/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```
### resolve the staticfiles 404:

because Django will handle the request for the static file only when the `DEBUG` option in settings is `True`, if run in production env, developer must handle it by himself.

1. declare the `STATIC_ROOT` in `settings.py`, or your custom setting files
2. install `whitenoise` via pip and edit the [`wsgi.py`](robot_view/wsgi.py) in `robot_view`

```shell
pip install whitenoise

# export the dependencies in requirements.txt
pip freeze > ./requirements.txt
```
```py
+ from whitenoise.django import DjangoWhiteNoise
+ application = DjangoWhiteNoise(application)
```
3. then run this command:

```shell
# collect the static file from the package like rest-framework
# to the STATIC_ROOT path where declare in settings file
python manage.py collectstatic
```
4. then rebuild the docker image and run it

```shell
# -d option can make the process in daemon mode.
docker-compose build && docker-compose up -d
```
### and schema and docs

django rest framework already support the docs and schema itself, just [include it and add a urlpatterns](apps/snippets/urls.py) is enough:

```py
+ from rest_framework.schemas import get_schema_view
+ from rest_framework.documentation import include_docs_urls
  urlpatterns = [
    path('', include(router.urls)),
    + path('schema/', schema_view),
    + path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
  ]
```