from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters as drf_filter
from .models import Museum
from .serializer import MuseumSerializer, MuseumFilter, MuseumListSerializer


class MuseumViewSet(viewsets.ModelViewSet):
    queryset = Museum.objects.all()
    filter_backends = (drf_filter.SearchFilter, drf_filter.OrderingFilter, DjangoFilterBackend)
    filterset_class = MuseumFilter
    filterset_fields = ['name', 'location', 'state__name']
    search_fields = ['name', 'location', 'state__name']
    ordering_fields = ['state__name']

    def get_serializer_class(self):
        if self.action == 'list':
            return MuseumListSerializer
        return MuseumSerializer
