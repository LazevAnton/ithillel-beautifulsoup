from django.shortcuts import render

from imdb.models import Movies
from service import ScrapeService


# Create your views here.
def index(request):
    movies_service = ScrapeService()
    movies = movies_service.get_top_movies()
    for top_movie in movies:
        movie = (
            Movies.objects.filter(
                title=top_movie.get('Title'),
                year=top_movie.get('Year')
            ).first()
        )
        if movie:
            movie.movie_poster = top_movie.get('Poster'),
            movie.rating = top_movie.get('Rating')
        else:
            movie = Movies(
                movie_poster=top_movie.get('Poster'),
                title=top_movie.get('Title'),
                year=top_movie.get('Year'),
                rating=top_movie.get('Rating')
            )
            movie.save()
    return render(request, 'core/index.html')
