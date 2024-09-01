
from django.urls import path
from . import views


urlpatterns = [
    path('', views.extractSalonInfoView, name="home"),
    path("register/", views.RegistrationView, name="register"),
    path('profile/', views.profileView, name='profile'),
]