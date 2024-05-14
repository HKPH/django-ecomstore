from django.urls import path
from .views import ProductSearch

urlpatterns = [
    path('api/search/', ProductSearch.as_view(), name='product-search'),
]