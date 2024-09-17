from django.db import models



class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salon_service = models.ForeignKey('salons.SalonService', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking by {self.customer.user.username} for {self.salon_service.service.service_name}'
