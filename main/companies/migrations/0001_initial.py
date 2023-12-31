# Generated by Django 4.1 on 2023-11-14 14:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Название компании"),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="E-mail адрес"),
                ),
                ("address", models.CharField(max_length=200, verbose_name="Адрес")),
                (
                    "logo",
                    models.ImageField(
                        upload_to="companies/logo/", verbose_name="Логотип компании"
                    ),
                ),
                ("website", models.URLField(verbose_name="Сайт компании")),
                (
                    "team_size",
                    models.PositiveIntegerField(verbose_name="Численность компании"),
                ),
                (
                    "year_founded",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2100),
                        ],
                        verbose_name="Год основания",
                    ),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Industry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Отрасль",
                "verbose_name_plural": "Отрасли",
            },
        ),
        migrations.CreateModel(
            name="ServiceCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="companies.servicecategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=18, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="phones",
                        to="companies.company",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="companies",
                to="companies.city",
                verbose_name="Город",
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="industries",
            field=models.ManyToManyField(
                related_name="companies",
                to="companies.industry",
                verbose_name="Отрасли",
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="services",
            field=models.ManyToManyField(
                related_name="companies", to="companies.service", verbose_name="Услуги"
            ),
        ),
    ]
