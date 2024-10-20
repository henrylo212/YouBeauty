
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from customers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),

    # THIS INCLUDES THE LOGIN VIEW!! There's a built in login view in Django!

    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # Make sure this is first to override default values later in django.auth.urls.
    # path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
    # path("accounts/salon_login/", auth_views.LoginView.as_view(template_name="registration/business_login.html")),

    


   
    # path("accounts/logout/", auth_views.LogoutView.as_view),

    path('', include("customers.urls")),
    path('salons/', include(('salons.urls', 'salons'), namespace='salons')),
    path('', include("customers.urls")),
    path('salon/', include('salons.urls')),
    path('customer/', include('customers.urls')),
    path('book/<int:salon_service_id>/', views.make_bookings, name='make_bookings'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
