from django.urls import path, include
from .apps import NetworkConfig
from rest_framework.routers import DefaultRouter

from network import views

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'retailer', views.RetailerViewSet, basename='retailer')

urlpatterns = [
    path('', include(router.urls)),
]
