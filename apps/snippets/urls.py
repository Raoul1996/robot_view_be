from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from . import views

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title='Pastebin API')
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
