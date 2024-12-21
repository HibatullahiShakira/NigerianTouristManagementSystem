from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters as drf_filter
from .models import Cuisine
from .serializer import CuisineSerializer, CuisineFilter


class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    filter_backends = (drf_filter.SearchFilter, drf_filter.OrderingFilter, DjangoFilterBackend)
    filterset_class = CuisineFilter
    filterset_fields = ['name', 'food_class', 'food_health', 'tribe__name']
    search_fields = ['name', 'food_class', 'food_health', 'tribe__name']
    ordering_fields = ['tribe__name']
