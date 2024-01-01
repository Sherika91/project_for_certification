from rest_framework import viewsets, filters
from .models import Retailer
from .permissions import UserIsActive
from .serializers import RetailerSerializer


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']
    permission_classes = [UserIsActive]
