from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializers, ItemSerializers
from .models import Category, Item

class CategoryListCreateViewAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
class ItemListCreateViewAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

@api_view(http_method_names=['POST', 'GET'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializers(instance=categories, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        received_data = request.data
        serializer = CategorySerializers(data=received_data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

@api_view(http_method_names=['POST', 'GET'])
def item_list_create_api_view(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializers(instance=categories, many=True)
        return Response(serializer.data, status=200)

    if request.method == 'POST':
        received_data = request.data
        serializer = ItemSerializers(data=received_data)
        if serializer.is_valid():
            item = serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

