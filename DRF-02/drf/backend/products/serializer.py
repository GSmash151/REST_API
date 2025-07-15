# drf/backend/products/serializer.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  my_discount = serializers.SerializerMethodField(read_only=True)  
  class Meta:
    model = Product
    fields = [
      'title',
      'content',
      'price',
      'sale_price', 
      'my_discount'
    ]

  def get_my_discount(self, obj):
    try:
      return obj.get_discount()
    except:
      return None
   


  # class ProductSerializer(serializers.ModelSerializer):
  # my_discount = serializers.SerializerMethodField(read_only=True)  
  # class Meta:
  #   model = Product
  #   fields = [
  #     'title',
  #     'content',
  #     'price',
  #     'sale_price', 
  #     'my_discount'
  #   ]

  # def get_my_discount(self, obj):
  #   print(obj.id)
  #   return obj.get_discount()


# class ProductSerializer(serializers.ModelSerializer):
#   discount = serializers.SerializerMethodField(read_only=True)  
#   class Meta:
#     model = Product
#     fields = [
#       'title',
#       'content',
#       'price',
#       'sale_price', 
#       'discount'
#     ]

  # class ProductSerializer(serializers.ModelSerializer):
  # class Meta:
  #   model = Product
  #   fields = [
  #     'title',
  #     'content',
  #     'price',
  #     'sale_price', 
  #     'get_discount'
  #   ]