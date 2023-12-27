from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class AuthorView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer

class PublisherView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = PublisherSerializer

class LanguageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = LanguageSerializer
