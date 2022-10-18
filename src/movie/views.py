from django.shortcuts import render
from .models import Movie

# Create your views here.

def movies_list(request):
    movies = Movie.objects.all()
    
    lastest_4 = Movie.objects.all().order_by('-id')[:4]
    
    context = {'movies': movies, 'movies_4': lastest_4}
    return render(request, 'movie/movies_list.html', context)


def movie_details(request):
    
    context = {}
    return render(request, 'movie/movie_detail.html', context)