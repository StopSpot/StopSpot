from django.shortcuts import render
from .models import bus_stop
from .models import stop_instance
import time
import json
import plotly.offline as py
import plotly.graph_objs as go
import by_stop_analysis as bs


def home(request):
    # time.time() is in seconds
    begin = time.time()

    greaterThan = 30

    # get all bus stops. Get all stop
    bus_stops = bus_stop.objects.all()
    stop_instances = stop_instance.objects.filter(door=1)
    stop_instances_gt30 = stop_instance.objects.filter(door=1, location_distance__gte=30)
    total_stop_dict = {}
    greaterThan_stop_dict = {}
    pct_error_dict = {}

    # Add more info to the header here
    pct_error_dict['Header'] = ("Stop Code", "Percent Error", "Total Stops", 'Stops Greater Than ' + str(greaterThan))

    for stop in bus_stops.iterator():
        total_stop_dict[stop.stop_code] = 0
        greaterThan_stop_dict[stop.stop_code] = 0

    for stop in stop_instances.iterator():
        try:
            total_stop_dict[stop.location_id] += 1
            if (stop.location_distance > 30):
                greaterThan_stop_dict[stop.location_id] += 1
        except:
            continue

    for stop in total_stop_dict:
        try:
            pct_error_dict[stop] = (
            round(greaterThan_stop_dict[stop] / total_stop_dict[stop], 3), total_stop_dict[stop],
            greaterThan_stop_dict[stop])
        except:
            continue

    num_stops = 0
    gt80_pct = 0
    for stop in pct_error_dict:
        num_stops += 1
        if stop != 'Header' and pct_error_dict[stop][0] > .8:
            print(str(stop) + "pct error: " + str(pct_error_dict[stop]))
            gt80_pct += 1

    # For debugging. Remove for production.
    print("number of stops with greater than 80 pct error:" + str(gt80_pct))
    print("number of stops:" + str(num_stops))

    context = {}
    context['bus_stops'] = bus_stops
    context['pct_error_dict'] = json.dumps(pct_error_dict)
    end = time.time()
    print((end - begin) / 60)
    return render(request, 'SysMap/home.html', context)


def about(request):
    return render(request, 'SysMap/about.html', {'title': 'About'})


def single_stop(request, lat, long, code):
    stop_instances = stop_instance.objects.filter(location_id=code, door=1)
    number_instances = stop_instance.objects.filter(location_id=code, door=1).count()
    hist_div = bs.histogram_by_hour(code)
    box_div = bs.box_plot(code)
    bar_day_div = bs.bar_chart_week(code)
    bar_month_div = bs.bar_chart_month(code)

    context = {
        'lat': lat,
        'long': long,
        'code': code,
        'stop_instances': stop_instances,
        'number_instances': number_instances,
        'hist_div': hist_div,
        'box_div': box_div,
        'bar_day_div': bar_day_div,
        'bar_month_div': bar_month_div,
    }
    return render(request, 'SysMap/single_stop.html', context)


"""
    View for displaying per stop analysis charts
    calls functions from by_stop_analysis that create graphs based on the 
    location_id passed in
    Each chart is a div object and can be called in the top.html template
"""


def stop_hour(request, code):
    try:
        code
    except NameError:
        code = 0
    location_id = code

    hist_div = bs.histogram_by_hour(location_id)
    box_div = bs.box_plot(location_id)
    bar_week_div = bs.bar_chart_week(location_id)
    bar_month_div = bs.bar_chart_month(location_id)

    context = {
        'hist_div': hist_div,
        'box_div': box_div,
        'bar_week_div': bar_week_div,
        'bar_month_div': bar_month_div,
    }

    return render(request, "SysMap/top.html", context)
