
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomeView, name="home"),
    # path('make-bookings', views.MakeBookingsView, name='make_bookings'),
    path('happy-hour-deals', views.HappyHourView, name='happy_hour'),
    path('top-salons', views.TopSalonsView, name='top_salons'),
]