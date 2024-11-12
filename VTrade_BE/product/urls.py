from django.urls import path
from . import views

urlpatterns = [
    path('/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('/<slug:slug>-<uuid:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('/filter/', views.ProductList.as_view(), name='product-filter'),
]
