"""Serializers for the 'companies' endpoints of 'Api' application v1."""
from rest_framework import serializers

from companies.models import (
    City,
    Company,
    FavoritesList,
    Industry,
    Phone,
    Service,
    ServiceCategory,
)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ("id", "name")


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "name")


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ("id", "name")


class CustomServiceSerializer(ServiceSerializer):
    category = ServiceCategorySerializer()

    class Meta:
        model = Service
        fields = ("id", "name", "category")


class CompanySerializer(serializers.ModelSerializer):
    """Сериализатор получения компании."""

    city = CitySerializer()
    services = ServiceSerializer(many=True)
    is_favorited = serializers.SerializerMethodField(method_name="get_favorited")

    def get_favorited(self, obj):
        request = self.context.get("request")
        if request and not request.user.is_anonymous:
            return FavoritesList.objects.filter(user=request.user, company=obj).exists()
        return False

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "logo",
            "city",
            "description",
            "services",
            "is_favorited",
        )


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ("number",)


class CompanyDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    industries = IndustrySerializer(many=True)
    services = CustomServiceSerializer(many=True)
    is_favorited = serializers.SerializerMethodField(method_name="get_favorited")
    phones = PhoneSerializer(many=True)

    def get_favorited(self, obj):
        request = self.context.get("request")
        if request and not request.user.is_anonymous:
            return FavoritesList.objects.filter(user=request.user, company=obj).exists()
        return False

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        phones = representation.get("phones", [])
        phone_numbers = [phone["number"] for phone in phones]
        representation["phones"] = phone_numbers
        return representation

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "description",
            "email",
            "phones",
            "city",
            "address",
            "industries",
            "services",
            "logo",
            "website",
            "team_size",
            "year_founded",
            "is_favorited",
        )


class CompanyFavoriteSerializer(serializers.ModelSerializer):
    """Список избранных компаний."""

    company = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ("id", "name", "logo", "city", "description", "services", "company")
