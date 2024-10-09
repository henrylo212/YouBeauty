
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from customers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("customers.urls")),
    path('salons/', include(('salons.urls', 'salons'), namespace='salons')),
    path('', include("customers.urls")),
    # path('salon/', include('salons.urls')),
    path('customer/', include('customers.urls')),
    path('book/<int:salon_service_id>/', views.make_bookings, name='make_bookings'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
