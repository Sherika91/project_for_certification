from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Retailer
from .permissions import UserIsActive
from .serializers import RetailerSerializer


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city', 'street', 'name']
    permission_classes = [UserIsActive, IsAuthenticated]
