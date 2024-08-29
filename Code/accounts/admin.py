from django.contrib import admin
from .models import SalonAddress, UserType, Users, SalonInfo, CustomerInfo

admin.site.register(SalonAddress)
admin.site.register(UserType)
admin.site.register(Users)
admin.site.register(SalonInfo)
admin.site.register(CustomerInfo)
