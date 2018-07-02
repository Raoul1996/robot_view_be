from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '.raoul1996.cn', '123.207.252.230']
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
