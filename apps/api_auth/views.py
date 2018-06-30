from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer
from users.serializers import User

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
