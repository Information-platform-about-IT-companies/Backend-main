"""Database settings of the 'Companies' app."""

from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="companies/logo/")
    website = models.URLField()
    services = models.ManyToManyField(
        Service,
        related_name="companies",
    )
    industries = models.ManyToManyField(
        Industry,
        related_name="companies",
    )
    team_size = models.PositiveIntegerField()
    year_founded = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100),
        ],
    )

    def __str__(self):
        return self.name


class Phone(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="phones",
    )
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.phone
