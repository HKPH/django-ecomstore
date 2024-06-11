from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
class CreateReview(APIView):
    def post(self, request):
        print(request.data)
        product_id = request.data.get('product_id')
        product_type = request.data.get('product_type')
        star = request.data.get('star')
        comment = request.data.get('comment')
        if not all([product_id, product_type, star, comment]):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            review = Review(
                product_id=product_id,
                product_type=product_type,
                star=star,
                comment=comment
            )
            review.save()
            return Response({'message': 'Review created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetReviewByProductIdAndType(APIView):
    def get(self, request, product_id, product_type, format=None):
        reviews = Review.objects.filter(product_id=product_id, product_type=product_type)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
