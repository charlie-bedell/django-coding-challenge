from django.db import models
from django.db.models import Avg
from math import floor


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()

    @property
    def runtime_formatted(self):
        # chose not to save to DB, runs each time runtime_formatted
        # is accessed
        rt = self.runtime
        return f"{rt // 60}:{rt % 60}"

    @property
    def avg_rating(self):
        avg = self.reviewers.aggregate(Avg('rating'))['rating__avg']
        if avg is None:
            return 0
        else:
            return round(avg, 2)
