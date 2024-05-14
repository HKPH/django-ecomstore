from django.urls import path
from .views import RegistrationView, LoginView, HomeView, UserProfileView,SearchView,AddToCartView,CartView,CreateOrderView,OrderListView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/create', CreateOrderView.as_view(), name='create_order'),
    path('order', OrderListView.as_view(), name='order'),
    
]
