from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer() # Nested serializer

    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection']
    
    # Custom validation (shows you know logic)
    def validate_unit_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be positive')
        return value