from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'subcategory',
            'title',
            'slug',
            'price',
            'image',
            'preview',
            'thumb'
        ]
