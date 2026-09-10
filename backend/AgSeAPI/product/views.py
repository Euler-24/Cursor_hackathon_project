from django.http import JsonResponse
from .models import Product

from django.forms.models import model_to_dict 

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def api_view(request):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
    return Response(data)