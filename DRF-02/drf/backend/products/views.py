from itertools import product
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')    
    content = serializer.validated_data.get('content') or title
    if content is None:
      content = title   
    serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

























