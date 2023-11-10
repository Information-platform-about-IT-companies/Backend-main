"""Filters for endpoints of the Info group."""

from django.db.models import Case, IntegerField, Value, When
from django.urls import resolve
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied

SEARCH_PARAM_REQUIRED_URL_NAMES = {"cities_list", "search_services_companies_list"}


class InfoSearchFilter(filters.SearchFilter):
    """Filter for endpoints of the Info group."""

    search_param = "name"

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get(self.search_param)
        if resolve(request.path_info).url_name in SEARCH_PARAM_REQUIRED_URL_NAMES:
            if name is None or len(name) < 3:
                raise PermissionDenied(
                    "The 'name' query parameter must contain at least three characters."
                )

        return (
            queryset.annotate(
                relevance_to_search=Case(
                    When(name__istartswith=name, then=Value(1)),
                    When(name__icontains=name, then=Value(2)),
                    default=0,
                    output_field=IntegerField(),
                )
            )
            .exclude(relevance_to_search=0)
            .order_by("relevance_to_search", "name")
        )