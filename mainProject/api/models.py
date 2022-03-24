# from django.db import models
from djongo import models
from django import forms
import uuid
from api.modelsConstants import *

# Create your models here.
class appointment(models.Model):
  _id = models.ObjectIdField()
  appointmentId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  appointmentPlace  = models.CharField(
    max_length = 2,
    choices = PLACE_CHOICES,
    default = 'p1',
    blank=True
  )
  appointmentDay = models.DateTimeField(blank=True)
  personOne = models.CharField(
    max_length = 2,
    choices = PERSON_CHOICES,
    default = 'p1',
    blank=True
  )
  personTwo = models.CharField(
    max_length = 2,
    choices = PERSON_CHOICES,
    default = 'p1',
    blank=True
  )
  volunteer = models.CharField(max_length=100, blank=True, default='')
  durationTime = models.DurationField(blank=True)
  type = models.CharField(
    max_length = 2,
    choices = APPOINTMENT_TYPE_CHOICES,
    default = 't1',
    blank=True
  )
  report = models.TextField(blank=True)

  class Meta:
    ordering = ['appointmentDay']

  def __str__(self):
    return self.title

class author(models.Model):
  _id = models.ObjectIdField()
  authorId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  yearsOld = models.IntegerField(blank=True, )
  education = models.CharField(
    max_length = 7,
    choices = AUTHOR_EDUCATION_CHOICES,
    default = 'e0',
    blank=True, 
  )
  job = models.CharField(
    max_length = 7,
    choices = AUTHOR_JOB_CHOICES,
    default = 'j0',
    blank=True, 
  )
  relationship = models.CharField(
    max_length = 7,
    choices = AUTHOR_RELATIONSHIP_CHOICES,
    default = 'r0',
    blank=True, 
  )

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.title

class path(models.Model):
  _id = models.ObjectIdField() 
  pathId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  start = models.DateField()
  end = models.DateField(blank=True, )
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
  email = models.EmailField(blank=True)
  test = models.CharField(max_length=100, blank=True, default='')
  tel = models.CharField(max_length=20, blank=True, default='')
  birthdate = models.DateField()
  createdAt = models.DateTimeField(auto_now_add=True)
  lastAppointment = models.DateField(auto_now=True)
  citizenship = models.CharField(
    max_length = 2,
    choices = CITIZENSHIP_CHOICES,
    default = 'IT',
  )
  path = models.ArrayField(
    model_container=path
  )

  class Meta:
    ordering = ['lastAppointment']

  def __str__(self):
    return self.title