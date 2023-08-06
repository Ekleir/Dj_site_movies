from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MovieView(View):
    """Список фильмов"""

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'site_movie/movies.html', {'movie_list': movies})


class MovieDetailView(View):
    """Описание фильма"""

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'site_movie/movie_detail.html', {'movie': movie})
