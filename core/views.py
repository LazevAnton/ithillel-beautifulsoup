from django.shortcuts import render

from imdb.models import Movies, TVShows
from service import ScrapeService


# Create your views here.
def index(request):
    service = ScrapeService()
    movies = service.get_top_movies()
    tvshows = service.get_top_tvshows()
    for top_movie in movies:
        movie = (
            Movies.objects.filter(
                title=top_movie.get('Title'),
                year=top_movie.get('Year')
            ).first()
        )
        if movie:
            movie.posters = top_movie.get('Poster'),
            movie.rating = top_movie.get('Rating')
        else:
            movie = Movies(
                posters=top_movie.get('Poster'),
                title=top_movie.get('Title'),
                year=top_movie.get('Year'),
                rating=top_movie.get('Rating')
            )
            movie.save()
    for top_tvshow in tvshows:
        tvshow = (
            TVShows.objects.filter(
                title=top_tvshow.get('Title'),
                year=top_tvshow.get('Year')
            ).first()
        )
        if tvshow:
            tvshow.posters = top_tvshow.get('Posters'),
            tvshow.title = top_tvshow.get('Title')
        else:
            tvshow = TVShows(
                posters=top_tvshow.get('Posters'),
                title=top_tvshow.get('Title'),
                year=top_tvshow.get('Year'),
                rating=top_tvshow.get('Rating')
            )
            tvshow.save()
    return render(request, 'core/index.html')
