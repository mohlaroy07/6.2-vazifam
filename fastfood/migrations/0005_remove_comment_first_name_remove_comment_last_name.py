# Generated by Django 5.1.2 on 2024-11-04 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0004_remove_food_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='last_name',
        ),
    ]
