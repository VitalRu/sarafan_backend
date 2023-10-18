import os

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

from shoptree.settings import MEDIA_ROOT


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
        upload_to='images/category',
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
        upload_to='images/subcategory',
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
    price = models.DecimalField(
        max_digits=15, decimal_places=2, default=99.99
    )
    image = models.ImageField(
        'изображение продукта',
        upload_to='images/product/',
        default=None
    )
    preview_image = models.ImageField(
        'изображение продукта (превью)',
        upload_to='images/product/preview',
        blank=True,
        null=True
    )
    thumb_image = models.ImageField(
        'изображение продукта (миниатюра)',
        upload_to='images/product/thumb',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print('>>>', self.image.name)
        print('>>>', self.image.path)

        img = Image.open(self.image.path)
        filename = os.path.basename(self.image.name)

        base = (900, 900)
        img.thumbnail(base)
        img.save(self.image.path)

        preview = (300, 300)
        preview_dir = f'{MEDIA_ROOT}/images/product/preview/'
        if not os.path.exists(preview_dir):
            os.makedirs(preview_dir)
        img.thumbnail(preview)
        img.save(preview_dir + filename)

        thumb = (100, 100)
        thumb_dir = f'{MEDIA_ROOT}/images/product/thumb/'
        if not os.path.exists(thumb_dir):
            os.makedirs(thumb_dir)
        img.thumbnail(thumb)
        img.save(thumb_dir + filename)

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
