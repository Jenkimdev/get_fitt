# Generated by Django 3.2.25 on 2024-07-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240424_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='best_for',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_vegan',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]
