from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        gt = self.request.query_params.get("gt")
        lt = self.request.query_params.get("lt")

        queryset = super().get_queryset()
        try:
            if gt is not None:
                queryset = queryset.filter(runtime__gt=gt)
            elif lt is not None:
                queryset = queryset.filter(runtime__lt=lt)

            return queryset

        except TypeError:
            raise "gt and lt only accept numerical values"


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'
    lookup_field = 'id'
