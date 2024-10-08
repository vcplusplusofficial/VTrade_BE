from django.urls import path
from . import views

urlpatterns = [
    path('listings/<slug:slug>/', views.listing_detail, name='product_detail'),
]
