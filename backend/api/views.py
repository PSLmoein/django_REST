from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwarg):
    
    body= request.body
    data= {}
    try:
        data = json.load(body)
    except:
        pass
    print(data)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)

