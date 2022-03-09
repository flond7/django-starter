# from django.db import models
from djongo import models
from django import forms

# Create your models here.
class appointment(models.Model):
  PERSON_CHOICES = [
        ('p1', 'Person 1'),
        ('p2', 'Person 2'),
  ]
  PLACE_CHOICES = [
        ('p1', 'Place 1'),
        ('p2', 'Place 2'),
  ]
  APPOINTMENT_TYPE_CHOICES = [
        ('t1', 'Type 1'),
        ('t2', 'Type 2'),
  ]
  _id = models.ObjectIdField()
  appointmentPlace  = models.CharField(
    max_length = 2,
    choices = PLACE_CHOICES,
    default = 'p1',
  )
  appointmentDay = models.DateTimeField()
  personOne = models.CharField(
    max_length = 2,
    choices = PERSON_CHOICES,
    default = 'p1',
  )
  personTwo = models.CharField(
    max_length = 2,
    choices = PERSON_CHOICES,
    default = 'p1',
  )
  type = models.CharField(
    max_length = 2,
    choices = APPOINTMENT_TYPE_CHOICES,
    default = 't1',
  )
  report = models.TextField()

  class Meta:
    ordering = ['appointmentDay']

  def __str__(self):
    return self.title

class author(models.Model):
  _id = models.ObjectIdField()
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  yearsOld = models.IntegerField()

  class Meta:
    ordering = ['name']
    #abstract = True

  def __str__(self):
    return self.title

class path(models.Model):
  STATUS_CHOICES = [
        ('closed', 'Chiuso'),
        ('ongoing', 'In corso'),
  ]
  _id = models.ObjectIdField()
  start = models.DateTimeField()
  end = models.DateTimeField()
  status = models.CharField(
    max_length = 7,
    choices = STATUS_CHOICES,
    default = 'ongoing',
  )
  authors = models.ArrayField(
    model_container=author,
  )
  appointments = models.ArrayField(
    model_container=appointment,
  )
  
  
  class Meta:
    ordering = ['start']
    #abstract = True

  def __str__(self):
    return self.title

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
  path = models.EmbeddedField(
    model_container=path
  )

  report = models.TextField()

  class Meta:
    ordering = ['birthdate']

  def __str__(self):
    return self.title