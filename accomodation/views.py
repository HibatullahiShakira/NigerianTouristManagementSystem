from rest_framework import viewsets
from .models import Accommodation
from .serializers import AccommodationSerializer


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

