from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .movie import Movie


class Review(models.Model):
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False)

    movie = models.ForeignKey(Movie,
                              blank=False,
                              null=False,
                              on_delete=models.CASCADE,
                              to_field="id",
                              related_name='reviewers')

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
