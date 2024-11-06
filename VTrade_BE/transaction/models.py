import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from authuser.models import CustomUser


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    content = models.TextField()
    consumer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='transactions_as_consumer'
    )
    seller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='transactions_as_seller'
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    create_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"Transaction {self.id} between {self.consumer} and {self.seller} for {self.product}"
