from django.urls import path
from .views import CreateReview, GetReviewByProductIdAndType

urlpatterns = [
    path('api/create-review/', CreateReview.as_view(), name='create_review'),
    path('api/get-review/<int:product_id>/<str:product_type>/', GetReviewByProductIdAndType.as_view(), name='get_review_by_product_id_and_type'),
]
