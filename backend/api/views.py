from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwarg):
    return JsonResponse({'message':'this django api working'})
