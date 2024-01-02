from rest_framework import serializers
from network.models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    supplier = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Retailer
        fields = ['id', 'name', 'slug', 'email', 'country', 'city', 'street', 'house_number', 'date_created', 'supplier',
                  'dept_to_supplier', 'products']
        read_only_fields = ['dept_to_supplier']
