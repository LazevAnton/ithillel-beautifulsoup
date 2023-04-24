from django.shortcuts import render
from .models import Movies, TVShows


def top_movies(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, template_name='core/movies.html', context=context)


def top_tvshows(request):
    tvshows = TVShows.objects.all()
    context = {
        'tvshows': tvshows
    }
    return render(request, 'core/tvshows.html', context=context)
