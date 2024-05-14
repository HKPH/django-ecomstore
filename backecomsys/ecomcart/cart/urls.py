from django.urls import path
from .views import AddToCart,RemoveFromCart,CartView,GetCartByUserId,DeleteCartByUserId,RemoveAllFromCart

urlpatterns = [
    path('api/cart/add_to_cart/', AddToCart.as_view(), name='add-to-cart'),
    path('api/cart/remove_from_cart/', RemoveAllFromCart.as_view(), name='remove_from_cart'),
    path('api/cart/<int:user_id>/', CartView.as_view(), name='cart'),
    path('api/cart/add/', AddToCart.as_view(), name='add-cart'),
    path('api/cart/remove/', RemoveFromCart.as_view(), name='remove-cart'),
    path('api/cart/get_cart/<int:user_id>/', GetCartByUserId.as_view(), name='get-cart-by-user-id'),
    path('api/cart/delete/<int:user_id>/', DeleteCartByUserId.as_view(), name='delete_cart_by_id'),

]

    