from rest_framework import serializers

from movies.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "name",
            "rating",
        )
        extra_kwargs = {'movie': {'read_only': True}}

class ReviewWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "id",
            "name",
            "rating",
        )
        extra_kwargs = {'movie': {'read_only': True}}
