# Generated by Django 5.0.4 on 2024-04-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_comment_created_at_comment_modified_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ('-modified_at',)},
        ),
    ]