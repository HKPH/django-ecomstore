from django.db import models
import random

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(User)
        super().save(*args, **kwargs)
        
def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id