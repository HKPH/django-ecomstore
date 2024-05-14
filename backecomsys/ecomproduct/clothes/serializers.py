from rest_framework import serializers
from .models import Clothes,Style,Producer

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'
    def get_image_url(self,product):
        request = self.context.get('request')
        image_url=product.imgae.url
        return request.build_absolute-uri(image_url)
    
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'