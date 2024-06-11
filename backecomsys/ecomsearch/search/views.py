from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class ProductSearch(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        keyword = request.query_params.get('q')
        if category == 'all':
            book_response = requests.get('http://localhost:8001/api/books/search/', params={'name': keyword})
            books = book_response.json() if book_response.status_code == status.HTTP_200_OK else []

            clothes_response = requests.get('http://localhost:8001/api/clothes/search/', params={'name': keyword})
            clothes = clothes_response.json() if clothes_response.status_code == status.HTTP_200_OK else []

            mobiles_response = requests.get('http://localhost:8001/api/mobiles/search/', params={'name': keyword})
            mobiles = mobiles_response.json() if mobiles_response.status_code == status.HTTP_200_OK else []

            if not (books or clothes or mobiles):
                return Response({'message': 'Không tìm thấy sản phẩm nào phù hợp'}, status=status.HTTP_404_NOT_FOUND)
            
            response_data = {}
            if books:
                response_data['books'] = books
            if clothes:
                response_data['clothes'] = clothes
            if mobiles:
                response_data['mobiles'] = mobiles
            
            return Response(response_data)
        
        elif category in ['books', 'clothes', 'mobiles']:
            search_response = requests.get(f'http://localhost:8001/api/{category}/search/', params={'name': keyword})
            if search_response.status_code == status.HTTP_200_OK:
                return Response(search_response.json())
            else:
                return Response({'message': 'Không tìm thấy sản phẩm nào phù hợp'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Invalid category'}, status=status.HTTP_400_BAD_REQUEST)
