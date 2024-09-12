
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.extractSalonInfoView, name="home"),
    path("register/", views.RegistrationView, name="register"),
    path("faq/", views.FAQView, name="faq"),
    path('profile/', views.profileView, name='profile'),
    path('edit_profile/', views.editProfileView, name='edit_profile'),
    path("forBusiness/", views.forBusinessView, name="forBusiness"),
    path('bookings/', views.bookingsView, name = 'bookings'),

    path("forBusiness/", views.forBusinessView, name="forBusiness"),
    path('business-login/', views.business_login, name='business_login'),
    path('business-register/', views.RegistrationView, name="business_register"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
