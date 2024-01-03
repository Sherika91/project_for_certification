from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf.urls.static import static

from config import settings
from .views import UsersViewSet

from .apps import UsersConfig

app_name = UsersConfig.name

users_router = SimpleRouter()

users_router.register("users", UsersViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
