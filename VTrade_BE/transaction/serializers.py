from rest_framework import serializers
from .models import Transaction

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'product', 'content', 'consumer', 'seller', 'status',
                  'create_date', 'update_date', 'slug'

        ]
        read_only_fields = ['slug', 'create_date', 'update_date']
