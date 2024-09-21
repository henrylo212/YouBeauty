from django.urls import path
from . import views

urlpatterns = [
    path('<int:salon_id>/', views.SalonDetailView, name='salon_page'),
    path('register-salon/', views.SalonRegistrationView, name='salon_form'),
]
  