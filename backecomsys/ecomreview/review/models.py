import random
from django.db import models
from django.contrib.auth.models import User

def random_id(model):
    id_list = model.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            return id
class Review(models.Model):
    id = models.BigIntegerField(primary_key=True)
    product_id = models.IntegerField()
    product_type = models.CharField(max_length=20)
    star = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Review)
        super().save(*args, **kwargs)


