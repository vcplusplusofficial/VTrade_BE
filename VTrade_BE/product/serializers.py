from rest_framework import serializers
from .models import Product


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'seller_id', 'slug', 'title', 'location', 'description', 'price',
            'status', 'payment_method', 'category', 'condition', 'rating', 'clicked',
            'create_date', 'update_date'
        ]
        read_only_fields = ['slug', 'create_date', 'update_date']
