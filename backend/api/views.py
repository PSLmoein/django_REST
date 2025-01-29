from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwarg): 
    
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
       #print(type(serializer.data))
       instance = serializer.save()
       print(type(instance))
       data = serializer.data
       print(type(data))                   
    return Response(data)

