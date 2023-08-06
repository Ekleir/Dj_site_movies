from django.views.generic import ListView, DetailView

from .models import Movie


class MovieView(ListView):
    """Список фильмов"""

    model = Movie
    template_name = 'site_movie/movie_list.html'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Описание фильма"""

    model = Movie
    slug_field = 'url'
    template_name = 'site_movie/movie_detail.html'
