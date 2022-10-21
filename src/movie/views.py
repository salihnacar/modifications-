from django.shortcuts import render
from .models import Movie, Actor

# Create your views here.

def movies_list(request):
    movies = Movie.objects.all()
    
    lastest_4 = Movie.objects.all().order_by('-id')[:4]
    popular_4 = Movie.objects.all().order_by('rate')[:4]
    lastest_6 = Movie.objects.all().order_by('-id')[:6]
    
    context = {'movies': movies, 'movies_4': lastest_4, 'popular_4': popular_4, 'lastest_6': lastest_6}
    return render(request, 'movie/movies_list.html', context)


def movie_details(request, slug):
    movie = Movie.objects.get(slug=slug)
    
    context = {'movie': movie}
    return render(request, 'movie/movie_detail.html', context)


def actor_details(request, slug):
    actor = Actor.objects.get(slug=slug)
    movies = Movie.objects.filter(actors=actor.id)
    
    context = {'actor': actor, 'movies': movies}
    return render(request, 'movie/actor.html', context)


def all_movies(request):
    first_3 = Movie.objects.all().order_by('rate')[0:3]
    second_3 = Movie.objects.all().order_by('rate')[3:6]
    my_popular = zip(first_3, second_3)
    
    all_movies = Movie.objects.all().order_by('-id')
    print(all_movies)
    
    context = {'my_popular': my_popular, 'all_movies': all_movies}
    return render(request, 'movie/all_movies.html', context)