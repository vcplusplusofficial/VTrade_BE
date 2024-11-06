import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class CustomUser(AbstractUser):
    """
    Custom user model with additional fields and role-based properties.
    Uses UUID for primary key, includes bio, class year, phone number,
    and role for different user types.
    """
    ROLE_ADMIN = 'ADMIN'
    ROLE_SELLER = 'SELLER'
    ROLE_CUSTOMER = 'CUSTOMER'

    # Additional fields for user profile
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(blank=True, null=True)
    class_year = models.IntegerField(null=True, blank=True, default=datetime.now,)
    phone_number = PhoneNumberField(blank=True, null=True)
    create_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated at"), auto_now=True)

    # User role field with choices
    role = models.CharField(
        max_length=50,
        choices=[
            (ROLE_ADMIN, 'Admin'),
            (ROLE_SELLER, 'Seller'),
            (ROLE_CUSTOMER, 'Customer')
        ],
        default=ROLE_CUSTOMER
    )

    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a slug from the username, if it doesn't already exist
        if not self.slug:
            base_slug = slugify(self.username)
            self.slug = base_slug
            counter = 1
            # Ensure slug uniqueness by appending a counter if necessary
            while CustomUser.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_admin(self):
        return self.role == 'ADMIN'

    @property
    def is_seller(self):
        return self.role == 'SELLER'
