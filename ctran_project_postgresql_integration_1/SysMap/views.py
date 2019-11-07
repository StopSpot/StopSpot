from django.shortcuts import render
from .models import bus_stop
from .models import stop_instance
import time
import json

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
    #time.time() is in seconds
    begin = time.time()

    #get all bus stops. Get all stop 
    bus_stops = bus_stop.objects.all()
    stop_instances = stop_instance.objects.filter(door = 1)
    stop_instances_gt30 = stop_instance.objects.filter(door=1,location_distance__gte = 30)
    total_stop_dict = {}
    greaterThan_stop_dict = {}
    pct_error_dict = {}

    for stop in bus_stops.iterator():
        total_stop_dict[stop.stop_code] = 0
        greaterThan_stop_dict[stop.stop_code] = 0

    for stop in stop_instances.iterator():
        try:
            total_stop_dict[stop.location_id] += 1
            if(stop.location_distance > 30):
                greaterThan_stop_dict[stop.location_id] += 1
        except:
            continue
        
    for stop in total_stop_dict:
        try:
            pct_error_dict[stop] = greaterThan_stop_dict[stop]/total_stop_dict[stop]
        except:
            continue


 
    context = {
        'posts': posts
    }
    context['bus_stops'] = bus_stops
    context['pct_error_dict'] = json.dumps(pct_error_dict)
    end = time.time()
    print((end - begin)/60)
    return render(request, 'SysMap/home.html', context, bus_stops)


def about(request):
    return render(request, 'SysMap/about.html', {'title': 'About'})

def single_stop(request, lat, long, code):
    stop_instances = stop_instance.objects.filter(location_id = code, door=1)
    number_instances = stop_instance.objects.filter(location_id = code,door=1).count()
    context = {
        'lat' : lat,
        'long' : long,
        'code' : code,
        'stop_instances' : stop_instances,
        'number_instances' : number_instances
    }
    return render(request, 'SysMap/single_stop.html', context )


    
    