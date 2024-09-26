
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("customers.urls")),
    path('salons/', include(('salons.urls', 'salons'), namespace='salons')),
    path('', include("customers.urls")),
    # path('salon/', incl