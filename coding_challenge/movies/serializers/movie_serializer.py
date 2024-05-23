from rest_framework import serializers
from .review_serializer import ReviewSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    reviewers = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "reviewers",
            "avg_rating"
        )
