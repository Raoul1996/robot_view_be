"""robot_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from users.views import SMSCodeViewSet, UserViewSets
from info.views import RobotInfoViewSet
from robot.views import RobotDataViewSet
router = DefaultRouter()
schema_view = get_schema_view(title="Server Monitoring API")

router.register(r'users', UserViewSets, base_name='users')
router.register(r'code', SMSCodeViewSet, base_name='code')
router.register(r'info', RobotInfoViewSet, base_name='info')
router.register(r'robot', RobotDataViewSet, base_name='robot')
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='robot_view documents')),
    path('admin/', admin.site.urls),
    path('schema/', schema_view),
    path('login/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token)
]
