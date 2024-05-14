from django.db import models
import random
class Producer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Producer)
        super().save(*args, **kwargs)
class Type(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Type)
        super().save(*args, **kwargs)
class Mobiles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    description = models.TextField()
    image = models.ImageField(upload_to='mobile_images/')
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Mobiles)
        super().save(*args, **kwargs)


def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id