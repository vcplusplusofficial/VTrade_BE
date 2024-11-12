from rest_framework import serializers
from .models import Product


class SellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug', 'create_date', 'update_date']


class CustomerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['clicked', 'update_date']
