from django.db import models
from django.db import models
import random

class Author(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Author)
        super().save(*args, **kwargs)

class Publisher(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Publisher)
        super().save(*args, **kwargs)

class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Category)
        super().save(*args, **kwargs)


class Book(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/')
    categories = models.ManyToManyField(Category)
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = random_id(Book)
        super().save(*args, **kwargs)
        
def random_id(module):
    id_list = module.objects.values_list('id', flat=True)
    while True:
        id = random.randint(1, 1_000_000_000)
        if id not in id_list:
            break
    return id