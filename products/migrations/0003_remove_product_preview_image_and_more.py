# Generated by Django 4.0.1 on 2023-10-18 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='preview_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='thumb_image',
        ),
    ]