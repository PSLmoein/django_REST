from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwarg):
    print(request.GET) #url query params
    body= request.body
    print(body)
    data= {}
    try:
        data = json.loads(body) #String of JSON data -> python dict
    except:
        pass
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    
    return JsonResponse(data)

