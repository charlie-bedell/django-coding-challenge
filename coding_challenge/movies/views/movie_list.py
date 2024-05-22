from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
