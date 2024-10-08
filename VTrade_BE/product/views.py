from django.shortcuts import get_object_or_404, render
from .models import Product

def listing_detail(request, slug):
    listing = get_object_or_404(Product, slug=slug)
    return render(request, 'listing_detail.html', {'listing': listing})
