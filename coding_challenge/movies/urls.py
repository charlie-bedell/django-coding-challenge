from django.urls import path

from movies.views import MovieListView, MovieDetailView, ReviewCreateView, ReviewUpdateDestroyView

urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:movie_id>/", MovieDetailView.as_view(), name="MovieDetailView"),
    path("<int:movie_id>/reviews/", ReviewCreateView.as_view(), name="ReviewCreateView"),
    path("<int:movie_id>/reviews/<int:review_id>", ReviewUpdateDestroyView.as_view(), name="ReviewUpdateDestroyView"),
]
