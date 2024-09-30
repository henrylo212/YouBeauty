
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.extractSalonInfoView, name="home"),
    path('make-bookings', views.MakeBookingsView, name='make_bookings'),
]