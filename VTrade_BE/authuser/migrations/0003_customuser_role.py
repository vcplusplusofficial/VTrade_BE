# Generated by Django 5.1.1 on 2024-10-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0002_alter_customuser_class_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SELLER', 'Seller'), ('CUSTOMER', 'Customer')], default='CUSTOMER', max_length=50),
        ),
    ]