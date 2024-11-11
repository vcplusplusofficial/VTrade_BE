from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'bio', 'class_year',
            'phone_number', 'create_date', 'update_date', 'role', 'slug'
        ]
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']
