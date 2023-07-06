# Generated by Django 4.2.2 on 2023-06-29 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muskeer', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_like', to=settings.AUTH_USER_MODEL),
        ),
    ]