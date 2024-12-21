from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Tour
from .serializer import TourSerializer, TourListSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['name', 'location', 'start_date', 'end_date']
    search_fields = ['name', 'location', 'start_date', 'end_date']
    ordering_fields = ['name', 'start_date', 'end_date']

    def get_serializer_class(self):
        if self.action == 'list':
            return TourListSerializer
        return TourSerializer
