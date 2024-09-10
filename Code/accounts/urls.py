
from django.urls import path
from . import views


urlpatterns = [
    path('', views.extractSalonInfoView, name="home"),
    path("register/", views.RegistrationView, name="register"),
    path("faq/", views.FAQView, name="faq"),
    path('profile/', views.profileView, name='profile'),

    path('bookings/', views.bookingsView, name = 'bookings'),

    path("forBusiness/", views.forBusinessView, name="forBusiness"),
    path('business-login/', views.business_login, name='business_login'),
    path('business-register/', views.RegistrationView, name="business_register"),

]