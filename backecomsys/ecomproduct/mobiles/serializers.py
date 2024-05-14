from rest_framework import serializers
from .models import Mobiles,Type,Producer

class MobilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiles
        fields = '__all__'
    def get_image_url(self,product):
        request = self.context.get('request')
        image_url=product.imgae.url
        return request.build_absolute-uri(image_url)
    
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'