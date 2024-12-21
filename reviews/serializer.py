from rest_framework import serializers

from reviews.models import Review
from tours.models import Tour


class UserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=50)


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        field = ['id', 'name', 'description', 'price', 'start_date', 'end_date', 'images', 'location', 'availability']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField
    tour = TourSerializer()

    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'user', 'tour', 'title', 'date']
