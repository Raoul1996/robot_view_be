from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'robot',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1'
        }
}
