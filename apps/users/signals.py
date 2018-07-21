from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # create or not, because when update, it will also post_save
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
