
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("customers.urls")),
    path('salons/', include(('salons.urls', 'salons'), namespace='salons')),
    path('', include("customers.urls")),
    # path('salon/', include('salons.urls')),
    path('customer/', include('customers.urls')),
]

