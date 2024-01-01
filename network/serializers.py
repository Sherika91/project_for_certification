from rest_framework import serializers
from network.models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'created_at', 'supplier',
                  'dept_to_supplier', 'products']
        read_only_fields = ['dept_to_supplier']
