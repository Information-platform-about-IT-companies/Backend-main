"""Views for 'companies' endpoints of 'Api' application v1."""

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.v1.companies.paginations import CustomPagination
from api.v1.companies.serializers import (
    CompanyDetailSerializer,
    CompanyFavoriteSerializer,
    CompanySerializer,
)
from companies.models import Company, FavoritesList


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    pagination_class = CustomPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("city", "services", "industries")

    def get_serializer_class(self):
        if self.action == "list":
            return CompanySerializer
        return CompanyDetailSerializer

    @action(detail=True, methods=["post", "delete"])
    def favorite(self, request, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response(
                {"detail": "Учетные данные не были предоставлены."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        company = get_object_or_404(Company, id=kwargs["pk"])
        if request.method == "POST":
            if FavoritesList.objects.filter(user=user, company=company).exists():
                raise exceptions.ValidationError(
                    "Компания добавлена в избранное ранее."
                )
            FavoritesList.objects.create(user=user, company=company)
            serializer = CompanyFavoriteSerializer(
                company,
                context={"request": request},
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == "DELETE":
            favoriteslist = FavoritesList.objects.filter(
                user=user, company=company
            ).first()
            if not favoriteslist:
                return Response(
                    {"detail": "Компании не было в избранном"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            favoriteslist.delete()
            return Response(
                {"detail": "Компания успешно удалена из избранного."},
                status=status.HTTP_204_NO_CONTENT,
            )
