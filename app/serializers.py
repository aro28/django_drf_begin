from rest_framework import serializers

from .models import Category, Item

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# class ItemSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'
class ItemSerializers(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def validate_name(self, value):
        excluded_chars = "●!#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~"
        for char in value:
            if char in excluded_chars:
                raise serializers.ValidationError(f"Символ {[char]} запрещен в имени. ")

    def validate(self, data):
        if not Category.objects.filter(id=data['category_id']).exist():
            raise  serializers.ValidationError('Такой категории не существует')
        raise data
    def create(self, validated_data):
        return Item.objects.create(
            name = validated_data['name'],
            price = validated_data['price'],
            category_id = validated_data['category_id'],
                )
    def update(self, instance, validated_data):
        pass