# Generated by Django 5.0.4 on 2024-04-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatar/'),
        ),
    ]
