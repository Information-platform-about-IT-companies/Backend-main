# Generated by Django 4.1 on 2023-12-19 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0008_alter_favorite_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="date_added",
            field=models.DateTimeField(
                default=datetime.datetime.today,
                verbose_name="Дата добавления в избранное",
            ),
        ),
    ]
