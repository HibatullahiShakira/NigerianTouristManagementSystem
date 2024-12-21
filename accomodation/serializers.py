from rest_framework import serializers

from accomodation.models import Accommodation
from tours.models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'name', 'description', 'price', 'start_date', 'end_date', 'images', 'location', 'availability']


class AccommodationSerializer(serializers.ModelSerializer):
    tour = TourSerializer()

    class Meta:
        model = Accommodation
        fields = ['id', 'location', 'availability', 'price', 'images', 'accommodation_type', 'accommodation_type',
                  'tour']
