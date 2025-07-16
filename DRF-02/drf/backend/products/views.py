# drf/backend/products/views.py

from rest_framework import status
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializer import ProductSerializer


"""ListCreateAPIView"""
class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [authentication.SessionAuthentication ]
  permission_classes = [permissions.IsAuthenticated]
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')    
    content = serializer.validated_data.get('content') or title
    if content is None:
      content = title   
    serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


"""CreateAPIView"""
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


"""DetailAPIView"""
class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


"""UpdateAPIView"""
class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title
      instance.save()

product_update_view = ProductUpdateAPIView.as_view()


"""DestroyAPIView"""
class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()


"""ListAPIView"""
# class ProductListAPIView(generics.ListAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer

# product_List_view = ProductListAPIView.as_view()


"""product_alt_view"""
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
    queryset = Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
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


""" Mixins"""
class ProductMixinView(
  mixins.DestroyModelMixin,
  mixins.CreateModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(
      self, 
      request, 
      *args, 
      **kwargs
    ):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(
    self,
    request, 
    *args, 
    **kwargs
  ):  

        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title
        if content is None:
            content = "I'm doing cool stuff"
        serializer.save(content=content)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


product_mixin_view = ProductMixinView.as_view()
