import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from authuser.models import CustomUser


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    content = models.TextField()
    consumer_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='transactions_as_consumer'
    )
    seller_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='transactions_as_seller'
    )
    create_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated at"), auto_now=True)
