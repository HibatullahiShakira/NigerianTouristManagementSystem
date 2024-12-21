from rest_framework import serializers

from .models import State, Tribe, Cuisine, Museum


class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = ['id', 'name', 'description']


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name', 'food_class', 'image', 'description']


class MuseumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Museum
        fields = ['id', 'name', 'image', 'location', 'description']


class StateSerializer(serializers.ModelSerializer):
    tribes = TribeSerializer(many=True, read_only=True)
    museums = MuseumSerializer(many=True, read_only=True)
    dishes = CuisineSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['id', 'name', 'description', 'geopolitical_zones',
                  'tribes', 'dishes', 'museums']


class StateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'geopolitical_zones']
