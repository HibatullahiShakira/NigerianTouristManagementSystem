from rest_framework import serializers
from django_filters import rest_framework as filters
from museuems.models import Museum
from states.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'description', 'geopolitical_zones']


class MuseumSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Museum
        fields = ['id', 'name', 'description', 'location', 'image', 'state']


class MuseumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ['id', 'name', 'image']


class MuseumFilter(filters.FilterSet):
    tribe_name = filters.CharFilter(field_name="state__name", lookup_expr='icontains')

    class Meta:
        model = Museum
        fields = ['name', 'location', 'state__name']
