from rest_framework import generics
from .serializers import CategorySerializers, ItemSerializers
from .models import Category, Item

class CategoryListCreateViewAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers