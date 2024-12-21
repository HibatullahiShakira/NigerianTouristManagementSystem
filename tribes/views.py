from rest_framework import viewsets
from .models import Tribe
from .serializer import TribeSerializer


class TribeViewSet(viewsets.ModelViewSet):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer

