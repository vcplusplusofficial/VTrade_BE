# Generated by Django 5.1.1 on 2024-10-06 21:14

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('status', models.IntegerField(choices=[(0, 'Not Listed'), (2, 'Pending'), (1, 'Bought')], default=2)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('cash', 'Cash')], max_length=20)),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
                ('condition', models.CharField(choices=[('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')], max_length=20)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('clicked', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Number of interactions')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]
