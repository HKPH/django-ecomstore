from django.urls import path
from .views import MobilesList,MobilesById,MobilesSearchByName

urlpatterns = [
    path('api/mobiles/', MobilesList.as_view(), name='mobiles-list'),
    path('api/mobiles/<int:pk>/', MobilesById.as_view(), name='mobiles-detail'),
    path('api/mobiles/search/', MobilesSearchByName.as_view(), name='mobiles-search'),

]
