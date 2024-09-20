from django.db import models

# class UserType(models.Model):
#     '''
#     Table for different types of users - admin user, business user and customer
#     '''
#     type_id = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=255, choices=[('admin', 'admin'), ('business', 'business'), ('customer', 'customer')])

# class SalonAddress(models.Model):
#     address_id = models.AutoField(primary_key=True)
#     street = models.CharField(max_length=255)
#     suburb = models.CharField(max_length=255)
#     state = models.CharField(max_length=3, choices=[('NSW', 'NSW'), ('ACT', 'ACT'), ('VIC', 'VIC'), ('QLD', 'QLD'), ('SA', 'SA'), ('WA', 'WA'), ('NT', 'NT')])
#     postcode = models.CharField(max_length=255)

# class Users(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=255, choices=[('admin', 'admin'), ('business', 'business'), ('customer', 'customer')], default='customer') 
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     address = models.ForeignKey(SalonAddress, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class SalonInfo(models.Model):
#     salon_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     business_name = models.CharField(max_length=255)
#     address = models.ForeignKey(SalonAddress, on_delete=models.CASCADE)
#     salon_phone = models.CharField(max_length=255)
#     salon_email = models.CharField(max_length=255)

# class CustomerInfo(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)