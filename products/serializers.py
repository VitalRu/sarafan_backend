from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # preview_image = serializers.SerializerMethodField(read_only=True)
    # thumb_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'subcategory',
            'title',
            'slug',
            'price',
            'base_image',
            # 'preview_image',
            # 'thumb_image'
        ]

    # def get_preview_image(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.preview_image()

    # def get_thumb_image(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.thumb_image()
