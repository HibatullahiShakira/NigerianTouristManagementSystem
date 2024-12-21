from rest_framework import serializers
from django_filters import rest_framework as filters
from cuisines.models import Cuisine
from tribes.models import Tribe


class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = ['id', 'name', 'description', 'image',]


class CuisineSerializer(serializers.ModelSerializer):
    tribe = TribeSerializer()

    class Meta:
        model = Cuisine
        fields = ['id', 'name', 'description', 'food_class', 'food_health', 'image', 'tribe']


class CuisineFilter(filters.FilterSet):
    tribe_name = filters.CharFilter(field_name="tribe__name", lookup_expr='icontains')

    class Meta:
        model = Cuisine
        fields = ['name', 'food_class', 'food_health', 'tribe_name']
