from rest_framework import serializers
from .models import Book
from .models import Author, Publisher, Category
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def get_image_url(self,product):
        request = self.context.get('request')
        image_url=product.imgae.url
        return request.build_absolute-uri(image_url)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
