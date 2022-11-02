from django.shortcuts import render
from movie.models import Movie, Series
# Create your views here.

def about_page(request):
    count_movies = Movie.objects.all().count()
    count_series = Series.objects.all().count()
    
    context = {'count_movies': count_movies, 'count_series': count_series}
    return render(request, 'about/about_page.html', context)
