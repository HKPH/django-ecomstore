from django.contrib import admin
from .models import Book, Publisher, Author, Category

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Category)