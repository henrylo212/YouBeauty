from django.urls import path
from . import views

urlpatterns = [
    path('', views.extractSalonInfoView, name="home"),
]
  