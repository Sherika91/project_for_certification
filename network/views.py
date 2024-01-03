from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Retailer, Factory, IndividualSeller
from .permissions import UserIsActive, IsUserAdmin
from .serializers import RetailerSerializer, FactorySerializer, IndividualSellerSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city', 'street', 'name']

    default_permission = [AllowAny, ]
    permissions = {
        'create': [IsAuthenticated, UserIsActive],
        'list': [IsAuthenticated, UserIsActive],
        'retrive': [IsAuthenticated, UserIsActive, IsUserAdmin],
        'partial_update': [IsUserAdmin],
        'destroy': [IsUserAdmin],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class RetailerViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city', 'street', 'name']

    default_permission = [AllowAny, ]
    permissions = {
        'create': [IsAuthenticated, UserIsActive],
        'list': [IsAuthenticated, UserIsActive],
        'retrive': [IsAuthenticated, UserIsActive, IsUserAdmin],
        'partial_update': [IsUserAdmin],
        'destroy': [IsUserAdmin],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class IndividualSellerViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = IndividualSeller.objects.all()
    serializer_class = IndividualSellerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city', 'street', 'name']

    default_permission = [AllowAny, ]
    permissions = {
        'create': [IsAuthenticated, UserIsActive],
        'list': [IsAuthenticated, UserIsActive],
        'retrive': [IsAuthenticated, UserIsActive, IsUserAdmin],
        'partial_update': [IsUserAdmin],
        'destroy': [IsUserAdmin],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
