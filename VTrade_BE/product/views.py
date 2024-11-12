from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import SellerProductSerializer, CustomerProductSerializer


# View for listing all products and creating a new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = SellerProductSerializer
    permission_classes = [AllowAny]


# View for retrieving and updating a specific product by ID
class ProductDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retrieve the product based on 'id' from the URL
        try:
            product = Product.objects.get(id=self.kwargs['id'])
        except Product.DoesNotExist:
            raise NotFound("Product not found.")

        return product

    def get_serializer_class(self):
        # Determines which serializer to use based on whether the user is the seller
        product = self.get_object()
        if product.seller == self.request.user:
            return SellerProductSerializer
        return CustomerProductSerializer


# Custom view for listing products with flexible filtering
class ProductList(APIView):
    def get(self, request, format=None):
        # Retrieve filter parameters from query params
        name = request.query_params.get("name")
        category = request.query_params.get("category")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")

        products = Product.objects.all()

        if name:
            products = products.filter(name__icontains=name)

        if category:
            products = products.filter(category__iexact=category)

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        serializer = SellerProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
