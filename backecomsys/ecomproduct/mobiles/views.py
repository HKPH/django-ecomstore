from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mobiles
from .serializers import MobilesSerializer

class MobilesList(APIView):
    def get(self, request):
        mobiles = Mobiles.objects.all()
        serializer = MobilesSerializer(mobiles, many=True,context={"request":request})
        return Response(serializer.data)
class MobilesById(APIView):
    def get_object(self, pk):
        try:
            return Mobiles.objects.get(pk=pk)
        except Mobiles.DoesNotExist:
            return None

    def get(self, request, pk):
        mobiles = self.get_object(pk)
        if mobiles is not None:
            serializer = MobilesSerializer(mobiles,context={"request":request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
class MobilesSearchByName(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('name', '')
        
        if query:
            mobiles = Mobiles.objects.filter(name__icontains=query)
        else:
            mobiles = Mobiles.objects.all()
        
        serializer = MobilesSerializer(mobiles, many=True,context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)