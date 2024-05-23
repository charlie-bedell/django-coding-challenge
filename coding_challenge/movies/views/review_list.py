from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.http import Http404


from movies.models import Review, Movie
from movies.serializers import ReviewSerializer, ReviewWithIdSerializer


class ReviewCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewWithIdSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        movie_id = self.kwargs.get("movie_id")
        obj = queryset.filter(movie_id=movie_id)
        return obj

    def perform_create(self, serializer):
        movie_id = self.kwargs.get('movie_id')
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie)


class ReviewUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        queryset = self.get_queryset()
        movie_id = self.kwargs.get("movie_id")
        review_id = self.kwargs.get("review_id")

        try:
            obj = queryset.get(movie_id=movie_id, id=review_id)
            return obj
        except Review.DoesNotExist:
            raise Http404("review does not exist")
    
