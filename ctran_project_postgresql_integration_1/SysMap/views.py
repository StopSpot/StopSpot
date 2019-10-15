from django.shortcuts import render
from .models import bus_stop

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    bus_stops = bus_stop.objects.all()
    context = {
        'posts': posts
    }
    context['bus_stops'] = bus_stops 
    return render(request, 'SysMap/home.html', context, bus_stops)


def about(request):
    return render(request, 'SysMap/about.html', {'title': 'About'})

def single_stop(request, lat, long):
    context = {
        'lat' : lat,
        'long' : long,
    }
    return render(request, 'SysMap/single_stop.html', context )

