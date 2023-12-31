# Generated by Django 4.1 on 2023-11-30 18:04

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                max_length=30,
                validators=[
                    users.validators.validate_first_name_and_last_name_fields,
                    django.core.validators.MinLengthValidator(2),
                ],
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                max_length=30,
                validators=[
                    users.validators.validate_first_name_and_last_name_fields,
                    django.core.validators.MinLengthValidator(2),
                ],
                verbose_name="Фамилия",
            ),
        ),
    ]
