from django.urls import path
from .views import UserRegistration, UserLogin, UserProfile

urlpatterns = [
    path('api/register/', UserRegistration.as_view(), name='user-registration'),
    path('api/login/', UserLogin.as_view(), name='user-login'),
    path('api/users/<int:user_id>/', UserProfile.as_view()),
]
