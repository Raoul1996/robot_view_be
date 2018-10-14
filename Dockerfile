FROM python:3

MAINTAINER Dockerfiles

RUN  apt-get clean

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        git \
        supervisor \
        nginx &&\
    rm -rf /var/lib/apt/lists/*

RUN pip3 install uwsgi

ENV MYSQL_DATABASE_NAME robot
ENV EMAIL_HOST_USER neuq@neuq.edu
ENV EMAIL_HOST_PASSWORD neuq_django

# configure nginx and supervisor

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY service/django-uwsgi-nginx/nginx-app.conf /etc/nginx/site-available/default
COPY service/django-uwsgi-nginx/supervisor-app.conf /etc/supervisor/conf.d/

# install the three-part lib

COPY requirements.txt /code/robot/
#RUN pip3 install -r /code/robot/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
RUN pip3 install -r /code/robot/requirements.txt

# uwsgi.ini and uwsgi_params

COPY . /code/

EXPOSE 8000 9090

CMD ["supervisord", "-n"]
