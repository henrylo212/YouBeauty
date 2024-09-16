from django.contrib import admin
from .models import SalonAddress, SalonInfo, SalonOwner, Service, SalonService

admin.site.register(SalonAddress)
admin.site.register(SalonInfo)
admin.site.register(SalonOwner)
admin.site.register(Service)
admin.site.register(SalonService)
