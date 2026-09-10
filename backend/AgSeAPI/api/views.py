import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_view(request, *args, **kwargs):
    #  request est une instance de HttpRequest
    print(request.body)  # byte string
    data = json.loads(request.body)
    print(data)
    data['headers'] = dict(request.headers)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)