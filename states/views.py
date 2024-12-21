from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters as drf_filter
from .serializer import StateSerializer, StateListSerializer
from .models import State


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    filter_backends = (drf_filter.SearchFilter, drf_filter.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['name', 'geopolitical_zones']
    search_fields = ['name', 'geopolitical_zones']
    ordering_fields = ['geopolitical_zones']

    def get_serializer_class(self):
        if self.action == 'list':
            return StateListSerializer
        return StateSerializer
