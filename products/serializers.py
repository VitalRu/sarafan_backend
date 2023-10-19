from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Product, Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SlugRelatedField(
        many=True, read_only=True, slug_field='slug'
    )
    image = serializers.SerializerMethodField('get_image_url', read_only=True,)

    class Meta:
        model = Category
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='slug', source='subcategory.category', read_only=True
    )
    subcategory = SlugRelatedField(slug_field='slug', read_only=True)
    images = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Product
        exclude = ['preview_image', 'thumb_image']

    def get_image_url(self, obj):
        if obj.preview_image:
            return (obj.image.url, obj.preview_image.url, obj.thumb_image.url)
        return None
