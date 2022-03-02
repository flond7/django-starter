from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import womanSerializer
from .models import woman

# Create your views here.
@api_view(['FET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/woman-list/',
    'Detail View':'/woman/<str:pk>',
    'Create':'/woman-create/',
    'Update':'/woman-update/<str:pk>',
    'Delete':'/woman-delete/<str:pk>',
  }
  return Response(basicApi_urls)

def womanList(request):
  women = women.objects.all()
  serializer = womanSerializer(women, many=True)
  return Response (serializer.data)