from django.urls import path
from .views import top_movies, top_tvshows

urlpatterns = [
    path('movies/', top_movies, name='movies'),
    path('tvshows/', top_tvshows, name='tvshows')
]
