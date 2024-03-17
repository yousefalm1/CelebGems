# Generated by Django 4.2.11 on 2024-03-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_celeb_profile'),
        ('celeb_profile', '0002_celebprofile_associated_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebprofile',
            name='associated_products',
        ),
        migrations.AddField(
            model_name='celebprofile',
            name='added_products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]