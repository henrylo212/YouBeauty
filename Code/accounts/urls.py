
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import CustomerLoginView, BusinessLoginView

# Can raise and use views to give error messages too!!

urlpatterns = [
    # path('', views.extractSalonInfoView, name="home"),
    path("customer-register/", views.CustomerRegistrationView, name="customer_register"),
    path("faq/", views.FAQView, name="faq"),
    path("about/", views.AboutView, name="about"),
    path('profile/', views.profileView, name='profile'),
    # path('edit_profile/', views.editProfileView, name='edit_profile'),
    path("forBusiness/", views.forBusinessView, name="forBusiness"),
    path('bookings/', views.bookingsView, name = 'bookings'),

    path("business_dashboard_home/", views.BusinessProfileHomeView, name="business_profile_home"),
    path("business_dashboard_settings/", views.BusinessProfileSettingsView, name="business_profile_settings"),
    path("business_dashboard_calendar/", views.BusinessProfileCalendarView, name="business_profile_calendar"),
    path('business_booking/edit/<int:booking_id>/', views.business_edit_booking, name='business_edit_booking'),

    # path('salon-login/', views.salon_login, name='salon_login'),
    path('business-register/', views.SalonOwnerRegistrationView, name="salon_register"),
    
    path("login/", views.CustomerLoginView.as_view(), name='login'),
    path("business_login/", views.BusinessLoginView.as_view(), name='business_login'),

    # These are all built in views!
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('search_results', views.search_results, name='search_results'),
]
