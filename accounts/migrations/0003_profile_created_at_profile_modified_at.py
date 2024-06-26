# Generated by Django 5.0.4 on 2024-04-23 15:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='modified_at',
            field=models.TimeField(auto_now=True),
        ),
    ]
