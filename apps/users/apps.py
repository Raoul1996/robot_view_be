from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name='users management'

    def ready(self):
        import users.signals
