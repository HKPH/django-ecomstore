from django.urls import path
from .views import ClothesList,ClothesById,ClothesSearchByName

urlpatterns = [
    path('api/clothes/', ClothesList.as_view(), name='clothes-list'),
    path('api/clothes/<int:pk>/', ClothesById.as_view(), name='clothes-detail'),
    path('api/clothes/search/', ClothesSearchByName.as_view(), name='clothes-search'),

]
