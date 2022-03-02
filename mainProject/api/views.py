from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import womanSerializer
from .models import woman

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/woman-list/',
    'Detail View':'/woman/<str:pk>',
    'Create':'/woman-create/',
    'Update':'/woman-update/<str:pk>',
    'Delete':'/woman-delete/<str:pk>',
  }
  return Response(basicApi_urls)

@api_view(['GET'])
def womenList(request):
  women = woman.objects.all()
  serializer = womanSerializer(women, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def womenDetail(request, pk):
  women = woman.objects.get(id=pk)
  serializer = womanSerializer(women, many=False) # many=false returns one object
  return Response (serializer.data)