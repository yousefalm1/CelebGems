# Generated by Django 4.2.11 on 2024-04-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_on_home',
            field=models.BooleanField(default=False),
        ),
    ]
