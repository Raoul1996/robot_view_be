# robot_view_be

> robot attachment viewer backend

[![Build Status](https://travis-ci.org/Raoul1996/robot_view_be.svg?branch=prod)](https://travis-ci.org/Raoul1996/robot_view_be)
[![CircleCI](https://circleci.com/gh/Raoul1996/robot_view_be/tree/dev.svg?style=svg)](https://circleci.com/gh/Raoul1996/robot_view_be/tree/dev)

## Run in development env

### Install

```bash
pip3 install -r ./requirement.txt
```
### Run

```bash
python3 manage.py runserver --settings=robot_view.dev_settings
```
or

```bash
./dev_robot.sh
```
## Run in Production env

Please install the docker-compose before you use it.

```bash
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

```python
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
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
```python
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
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

```python
from rest_framework.schemas import get_schema_view
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
schema_view = get_schema_view(title="Server Monitoring API")

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='doc', description='desc'))
  ]
```
### Fix list is not callable

After configure the router for user app, in development env, app can work very will, when build docker container, app throw a error: **list object is not callable**

Solution is very easy: use the tuple, don't use list.

```python
# robot_view/setting.py
REST_FRAMEWORK = {
     # Use Django's standard `django.contrib.auth` permissions,
     # or allow read-only access for unauthenticated users.
     'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
     'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    )
}
```
### Change authorization method to JWT

- edit [setting.py](./robot_view/setting.py), and the `AUTHENTICATION_BACKENDS`

    ```python
    AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackend',
        'django.contrib.auth.backends.ModelBackend'
    )
    ```

- post the `username` and `password` to [http://127.0.0.1:8001/login/](http://127.0.0.1:8001/login/) to exchange the jwt
- and `Authorization` request header and `Bearer` prefix for jwt string

### Create thrift server in Django app

for rpc, I choose to use apache thrift framework

- install `django-thrift`:

    ```shell
    pip install django-thrift
    ```
- configure `django-thrift` in [setting.py](robot_view/settings.py)
    - add `'django_thrift'` in `INSTALLED_APPS`
    - add `THRIFT` configure option in [setting.py](/robot_view/settings.py)
    - add `FILE` option in `THRIFT` point to `*.thrift` file
    - add `SERVICE` option named is the same to the `thrift` server name

- write the thrift handler in django app `view`:

    ```python
    # import the create_handler
    from django_thrift.handler import create_handler

    # get a handler instantiation
    handler = create_handler()

    # defined the thrift method
    @handler.map_function("saveRobotData")
    def save_robot_data_handler():
        return {"a": "bb"}

    # more thrift methods can be defined
    ```

- management thrift server on localhost 9090

    ```bash
    # start rpc server
    python manage.py runrpcserver
    ```
### Create extra_app folder to store the library which have to modify the source code

Because I need change the thrift server listen host and port, but `django-thrift` library can't support change these in `setting.py`, so I have to modify the source code of this library.

- create `extra_app` folder

    ```bash
    mkdir extra_app
    ```
- move the `django-thrift` library from `site-package` to `extra-app`:

    ```bash
    mv to_your_site_package_path/django-thrift extra_app
    ```
- add `extra-app` in `PYTHONPATH` via modify the [setting.py](robot_view/settings.py)

    ```python
    import sys, os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
    ```
- modify the `django-thrift` source code what you want to edit.

### save password as django command 'createsuperuser'

before I do these, only the user which create via django manage.py command `createsuperuser` can generate current JSON WEB Token. So I want to know why.

the user Profile data store in `users_userporfile` table, the password field which user is created by command is encrypted, so I need use the same methods to encrypt the password before save it in database.

search in django source code, I find the [`make_password`](https://github.com/django/django/blob/stable%2F2.0.x/django/contrib/auth/hashers.py#L64) function, and when use create superuser, the manage.py don't provide the **salt**, so just use the like [base_user.py](https://github.com/django/django/blob/stable%2F2.0.x/django/contrib/auth/base_user.py#L97):

```python
from django.contrib.auth.hashers import make_password
def validate(self, attrs):
    attrs["raw_password"] = attrs["password"]
    attrs["password"] = make_password(attrs["password"])
    return attrs
```

### use `Q` and rewrite retrieve method add prop on response
the minimum code implementation : 

```python
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, response
from rest_framework.mixins import  RetrieveModelMixin
User = get_user_model()

class ExampleViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        re_dict = serializer.data
        re_dict["username"] = User.objects.get(Q(id=re_dict["user"])).username
        del re_dict["user"]
        headers = self.get_success_headers(serializer.data)
        return response.Response(re_dict, status=status.HTTP_200_OK, headers=headers)
```