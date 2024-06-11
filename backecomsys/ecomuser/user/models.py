# from django.db import models
# import random

# class User(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     birthday = models.DateField(null=True, blank=True)
#     email = models.EmailField(max_length=50, null=True, blank=True)
#     phone_number = models.CharField(max_length=10, null=True, blank=True)
#     address = models.CharField(max_length=50, null=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.id = random_id(User)
#         super().save(*args, **kwargs)
        
# def random_id(module):
#     id_list = module.objects.values_list('id', flat=True)
#     while True:
#         id = random.randint(1, 1_000_000_000)
#         if id not in id_list:
#             break
#     return id

from django.db import models
import random

def random_id(model):
    id_list = model.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    
    full_name = models.OneToOneField('FullName', on_delete=models.CASCADE, null=True, blank=True)
    account = models.OneToOneField('Account', on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(User)
        super().save(*args, **kwargs)

class FullName(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
