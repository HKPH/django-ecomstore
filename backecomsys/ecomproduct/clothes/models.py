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
class Style(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Style)
        super().save(*args, **kwargs)
class Clothes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='clothes_images/')
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Clothes)
        super().save(*args, **kwargs)

def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id