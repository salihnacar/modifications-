from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies'),
    path('movie_details/<slug:slug>', views.movie_details, name='movie_details'),
    path('actor/<slug:slug>', views.actor_details, name='actor'),
    path('all', views.all_movies, name="all"),
    path('type/<slug:slug>', views.movies_in_type, name='type'),
]