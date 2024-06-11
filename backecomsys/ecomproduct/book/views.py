from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book,Author, Publisher, Category
from .serializers import BookSerializer,AuthorSerializer, PublisherSerializer, CategorySerializer
from rest_framework import generics
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True,context={"request":request})
        return Response(serializer.data)
class BookById(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    def get(self, request, pk):
        book = self.get_object(pk)
        if book is not None:
            serializer = BookSerializer(book,context={"request":request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class AuthorById(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return None
    def get(self, request, pk):
        author = self.get_object(pk)
        if author is not None:
            serializer = AuthorSerializer(author, context={"request": request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class PublisherById(APIView):
    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return None
    def get(self, request, pk):
        publisher = self.get_object(pk)
        if publisher is not None:
            serializer = PublisherSerializer(publisher, context={"request": request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class CategoryById(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None
    def get(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = CategorySerializer(category, context={"request": request})
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class BookSearchByName(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('name', '')
        if query:
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books,many=True,context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)