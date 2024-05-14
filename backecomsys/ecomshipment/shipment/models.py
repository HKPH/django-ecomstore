from django.db import models
import random
class Shipment(models.Model):
    order_id = models.PositiveIntegerField()
    address = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=3)
    id = models.BigIntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Shipment)
        super().save(*args, **kwargs)
        
def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id