# from django.db import models
from djongo import models
from django import forms
from api.modelsConstants import *

# Create your models here.
class appointment(models.Model):
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
  volunteer = models.CharField(max_length=100, blank=True, default='')
  durationTime = models.DurationField()
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
  education = models.CharField(
    max_length = 7,
    choices = AUTHOR_EDUCATION_CHOICES,
    default = 'e0',
  )
  job = models.CharField(
    max_length = 7,
    choices = AUTHOR_JOB_CHOICES,
    default = 'j0',
  )
  relationship = models.CharField(
    max_length = 7,
    choices = AUTHOR_RELATIONSHIP_CHOICES,
    default = 'r0',
  )

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.title

class path(models.Model):
  _id = models.ObjectIdField()
  start = models.DateTimeField()
  end = models.DateTimeField()
  status = models.CharField(
    max_length = 7,
    choices = PATH_STATUS_CHOICES,
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

  def __str__(self):
    return self.title

class woman(models.Model):
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