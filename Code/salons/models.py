from django.db import models

class SalonAddress(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address_line1}, {self.state}, {self.country}'


class SalonInfo(models.Model):
    salon_name = models.CharField(max_length=255)
    salon_address = models.OneToOneField(SalonAddress, on_delete=models.CASCADE)
    salon_photo = models.ImageField(upload_to='salon_photos/', blank=True, null=True)
    salon_openingtime = models.TimeField()
    salon_closingtime = models.TimeField()
    happyhour_times = models.CharField(max_length=255)
    happyhour_days = models.CharField(max_length=255)
    happyhour_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.salon_name


class SalonOwner(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    salon = models.OneToOneField(SalonInfo, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} (Owner of {self.salon.salon_name})'

class Service(models.Model):
    service_name = models.CharField(max_length=255)

    def __str__(self):
        return self.service_name


class SalonService(models.Model):
    salon = models.ForeignKey(SalonInfo, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.service.service_name} at {self.salon.salon_name}'

