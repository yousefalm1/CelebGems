# Generated by Django 4.2.11 on 2024-04-11 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celeb_profile', '0005_celebprofile_display_on_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='celeb_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
