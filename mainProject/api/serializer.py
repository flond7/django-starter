from rest_framework import serializers
from .models import woman

class womanSerializer(serializers.ModelSerializer):
  class Meta:
    model = woman
    fields = '__all__'