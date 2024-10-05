from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# def CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Didn't provide valid e-mail")
#
#
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     bio = models.TextField(blank=True, null=True)
#     birth_date = models.DateField(blank=True, null=True)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Optional profile picture
#
#     def __str__(self):
#         return self.username  # Display the username in string representation
