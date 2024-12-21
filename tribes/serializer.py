from rest_framework import serializers

from states.models import State
from .models import Tribe


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'description', 'geopolitical_zones']


class TribeSerializer(serializers.ModelSerializer):
    state = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Tribe
        fields = ['id', 'name', 'description', 'image', 'state']
