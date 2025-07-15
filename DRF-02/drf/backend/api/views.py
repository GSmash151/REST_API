import json
from django.forms.models import model_to_dict
# from django.shortcuts import render 
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product



@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
  model_data = Product.objects.all().order_by('?').first()
  data = {}
  if model_data:
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
  return Response(data)



# @api_view(["GET", "POST"])
# def api_home(request, *args, **kwargs):
#   if request.method != "POST":
#     return Response({"detail": "GET not allowed"}, status=405)
#   model_data = Product.objects.all().order_by('?').first()
#   data = {}
#   if model_data:
#     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#   return Response(data)



# def api_home(request, *args, **kwargs):
#   model_data = Product.objects.all().order_by('?').first()
#   data = {}
#   if model_data:
#     data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#   return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#   model_data = Product.objects.all().order_by("?").first()
#   data = {}
#   if model_data:
#     data['id'] = model_data.id
#     data['title'] = model_data.title
#     data['content'] = model_data.content
#     data['price'] = model_data.price
#   return JsonResponse(data)


# Testing 
# def api_home(request, *args, **kwargs):
#   print(request.GET)
#   print(request.POST)
#   body = request.body
#   data = {}
#   try:
#     data = json.loads(body)
#   except:
#     pass
#   print(data)
#   data['params'] = dict(request.GET)
#   data['headers'] = dict(request.headers)
#   data['content_type'] = request.content_type  
#   return JsonResponse(data)

















