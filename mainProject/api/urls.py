from django.urls import path
from . import views
urlpatterns = [
  path('', views.apiOverview, name="api-overwiev"),
  path('women-list', views.womenList, name="women-list"),
]