from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie, Category
from .forms import ReviewForm


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

