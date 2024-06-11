from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Clothes
from .serializers import ClothesSerializer

class ClothesList(APIView):
    def get(self, request):
        clothes = Clothes.objects.all()
        serializer = ClothesSerializer(clothes, many=True,context={"request":request})
        return Response(serializer.data)
class ClothesById(APIView):
    def get_object(self, pk):
        try:
            return Clothes.objects.get(pk=pk)
        except Clothes.DoesNotExist:
            return None
    def get(self, request, pk):
        clothes = self.get_object(pk)
        if clothes is not None:
            serializer = ClothesSerializer(clothes,context={"request":request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class ClothesSearchByName(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('name', '')
        
        if query:
            clothes = Clothes.objects.filter(name__icontains=query)
        else:
            clothes = Clothes.objects.all()
        
        serializer = ClothesSerializer(clothes, many=True,context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)