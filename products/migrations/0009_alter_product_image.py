# Generated by Django 4.2.11 on 2024-04-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='product_img/'),
        ),
    ]
