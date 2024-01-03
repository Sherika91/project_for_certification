from rest_framework import serializers

from network.models import Retailer, Factory, IndividualSeller


class RetailerSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Retailer
        fields = '__all__'
        read_only_fields = ['dept_to_supplier']


class FactorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ['dept_to_supplier']


class IndividualSellerSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = IndividualSeller
        fields = '__all__'
        read_only_fields = ['dept_to_supplier']
