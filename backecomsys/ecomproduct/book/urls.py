from django.urls import path
from .views import BookList,BookById,CategoryById,AuthorById,PublisherById,BookSearchByName

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookById.as_view(), name='book-detail'),
    path('api/author/<int:pk>/', AuthorById.as_view(), name='author'),
    path('api/publisher/<int:pk>/', PublisherById.as_view(), name='publisher'),
    path('api/category/<int:pk>/', CategoryById.as_view(), name='category'),
    path('api/books/search/', BookSearchByName.as_view(), name='book-search'),
]
