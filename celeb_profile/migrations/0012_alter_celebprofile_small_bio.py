# Generated by Django 4.2.11 on 2024-04-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celeb_profile', '0011_alter_celebprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebprofile',
            name='small_bio',
            field=models.CharField(default='', max_length=100),
        ),
    ]
