from django.db import models
import random
class Payment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    order_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    payment_method = models.CharField(max_length=100)
    payment_datetime = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Payment)
        super().save(*args, **kwargs)
        
def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id