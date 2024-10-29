import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(blank=True, null=True)
    class_year = models.IntegerField(null=True, blank=True, default=datetime.now().year)
    phone_number = PhoneNumberField(blank=True, null=True)
    create_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated at"), auto_now=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('ADMIN', 'Admin'),
            ('SELLER', 'Seller'),
            ('CUSTOMER', 'Customer')
        ],
        default='CUSTOMER'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_admin(self):
        return self.role == 'ADMIN'

    @property
    def is_seller(self):
        return self.role == 'SELLER'
