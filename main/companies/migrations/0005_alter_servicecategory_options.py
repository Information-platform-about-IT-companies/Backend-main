# Generated by Django 4.1 on 2023-11-21 21:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0004_favoriteslist_favoriteslist_unique_favorite"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="servicecategory",
            options={
                "verbose_name": "Категория сервиса",
                "verbose_name_plural": "Категории сервисов",
            },
        ),
    ]
