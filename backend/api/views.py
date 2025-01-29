from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwarg): 
    instance = Product.objects.all().order_by("?").first()
    
    data = ProductSerializer(instance).data
                       
    return Response(data)

