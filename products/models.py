import os

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin


User = get_user_model()


class Category(models.Model):
    title = models.CharField('имя категории', max_length=32)
    slug = models.SlugField(
        'slug категории',
        max_length=32,
        unique=True,
    )
    image = models.ImageField(
        'изображение категории',
        upload_to='product/images/category',
        default=None,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, related_name='subcategory', on_delete=models.PROTECT
    )
    title = models.CharField(max_length=32)
    slug = models.SlugField(
        'slug подкатегории',
        max_length=32,
        unique=True,
    )
    image = models.ImageField(
        'изображение подкатегории',
        upload_to='product/images/subcategory',
        default=None,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return self.title


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory, related_name='product', on_delete=models.PROTECT
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(
        'slug продукта',
        max_length=32,
        unique=True,
    )
    base_image = models.ImageField(
        'изображение продукта',
        upload_to='product/images/product',
        default=None,
    )
    price = models.DecimalField(
        max_digits=15, decimal_places=2, default=99.99
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @property
    @admin.display(description='превью')
    def preview_image(self):
        with Image.open(self.base_image.path) as img:

            img.thumbnail(400, 400)
            preview_path = os.path.join(
                'product/images/product/preview', self.base_image.name
            )
            img.save(preview_path)
        return img

    @property
    @admin.display(description='миниатюра')
    def thumb_image(self):
        with Image.open(self.base_image.path) as img:
            img.thumbnail(100, 100)
            thumb_path = os.path.join(
                'product/images/product/thumb', self.base_image.name
            )
            img.save(thumb_path)
        return img

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shopping_items',
        verbose_name='пользователь списка покупок'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_cart_products',
        verbose_name='рецепт в списке покупок'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'product'),
                name='unique_shopping_list',
            ),
        )

    def __str__(self):
        return f"{self.product} in {self.user}'s cart"
