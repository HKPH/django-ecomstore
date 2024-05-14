from django.db import models
import random
class Order(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.PositiveIntegerField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Order)
        super().save(*args, **kwargs)
        

class OrderItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)
    product_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.PositiveIntegerField()
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(OrderItem)
        super().save(*args, **kwargs)
        
def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id