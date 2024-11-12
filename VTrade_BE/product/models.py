import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    STATUS_NOT_LISTED = 0
    STATUS_BOUGHT = 1
    STATUS_PENDING = 2

    STATUS_CHOICES = [
        (STATUS_NOT_LISTED, "Not Listed"),
        (STATUS_PENDING, "Pending"),
        (STATUS_BOUGHT, "Bought"),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title = models.CharField(_("Title"), max_length=255)
    location = models.CharField(_("Location"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(
        _("Price"),
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    category = models.CharField(_("Category"), max_length=255)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(5.00)
        ]
    )
    clicked = models.IntegerField(
        _("Number of interactions"),
        validators=[MinValueValidator(0)],
        default=0,
        blank=True
    )

    create_date = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated at"), auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            counter = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        permissions = [
            ("can_update_price", "Can update product price"),
            ("can_view_stock", "Can view stock levels"),
        ]

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    # image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True, help_text="Alternative text for the image")
