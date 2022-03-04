# from django.db import models
from djongo import models

# Create your models here.
class woman(models.Model):
  CITIZENSHIP_CHOICES = [
        ('IT', 'Italiana'),
        ('ST', 'Straniera'),
    ]
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  birthdate = models.DateTimeField()
  timestamp = models.DateTimeField(auto_now_add=True)
  citizenship = models.CharField(
    max_length = 2,
    choices = CITIZENSHIP_CHOICES,
    default = 'IT',
  )
  report = models.TextField()

  class Meta:
    ordering = ['birthdate']

  def __str__(self):
    return self.title