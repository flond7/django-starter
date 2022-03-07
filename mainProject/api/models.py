# from django.db import models
from djongo import models

# Create your models here.
class appointment(models.Model):
  ATTENDING_CHOICES = [
        ('none', ''),
        ('p1', 'Person One'),
        ('p2', 'Person Two'),
  ]
  PLACE_CHOICE = [
        ('none', ''),
        ('p1', 'Place One'),
        ('p2', 'Place Two'),
  ]
  appointmentDate = models.DateTimeField()
  appointmentPlace = models.CharField(
    max_length = 2,
    choices = PLACE_CHOICE,
    default = 'none',
  )
  status = models.CharField(
    max_length = 2,
    choices = ATTENDING_CHOICES,
    default = 'none',
  )
  report = models.TextField()

  class Meta:
    ordering = ['appointmentDate']
    abstract = True

  def __str__(self):
    return self.title


class author(models.Model):
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  yearsOld = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['name']
    abstract = True

  def __str__(self):
    return self.title


class path(models.Model):
  STATUS_CHOICES = [
        ('closed', 'Chiuso'),
        ('ongoing', 'In corso'),
  ]
  start = models.DateTimeField()
  end = models.DateTimeField()
  status = models.CharField(
    max_length = 2,
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
    abstract = True

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
    model_container=path,
  )
  report = models.TextField()

  class Meta:
    ordering = ['birthdate']

  def __str__(self):
    return self.title
