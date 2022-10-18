from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movies'),
    path('movie_details', views.movie_details, name='movie_details'),
]