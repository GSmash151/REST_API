from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Product
from .serializer import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
  qs = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')    
    content = serializer.validated_data.get('content') or title
    if content is None:
      content = title   
    serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductCreateAPIView(generics.CreateAPIView):
  qs = Product.objects.all()
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
  qs = Product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#   qs = Product.objects.all()
#   serializer_class = ProductSerializer

# product_List_view = ProductListAPIView.as_view()

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method 

  if method == "GET":
    if pk is not None:
        # detail view
        obj = get_object_or_404(Product, pk=pk)
        data = ProductSerializer(obj, many=False).data
        return Response(data)
    
    # list view
    qs = Product.objects.all()
    data = ProductSerializer(qs, many=True).data
    return Response(data)
  if method == "POST":
    # create an item 
     serializer = ProductSerializer(data=request.data)
     if serializer.is_valid(raise_exception=True):
        title = serializer.validated_data.get('title')    
        content = serializer.validated_data.get('content') or title
        if content is None:
          content = title   
          serializer.save(content=content)
        return Response(serializer.data)
  return RecursionError({"invalid": "not good data"}, status=status.HTTP_400_BAD_REQUEST)

























