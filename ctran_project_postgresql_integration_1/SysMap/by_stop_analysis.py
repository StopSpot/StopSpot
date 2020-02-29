from SysMap.models import stop_instance
import plotly.offline as py
import plotly.graph_objs as go
from decimal import Decimal

from django.db.models import Count
from django.db.models.functions import ExtractWeekDay, ExtractMonth, ExtractYear

out_of_bounds = 98.4252 #in feet

"""
    Returns a div object that contains a plotly histogram
    histogram displays number stops by hour for a location_id
    argument passed in is an int for the location id
"""


def histogram_by_hour(loc_id):
    out_b = stop_instance.objects.filter(door=1, location_distance__gt=out_of_bounds, location_id=loc_id).values_list(
        'leave_time', flat=True)
    out_list = list(out_b)
    o_con = [i / 60 / 60 for i in out_list]
    in_b = stop_instance.objects.filter(door=1, location_distance__lte=out_of_bounds, location_id=loc_id).values_list(
        'leave_time', flat=True)
    in_list = list(in_b)
    i_con = [i / 60 / 60 for i in in_list]
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=o_con, name='out of bounds stops'))
    fig.add_trace(go.Histogram(x=i_con, name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='In/Out of bounds by hour location_id ' + str(loc_id),
        xaxis_title='hour of day',
        yaxis_title='number of stop instances',
        barmode='overlay'
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div


"""
    Returns a div object that contains a plotly box plot
    box plot displays distribution of location_distances
    all stop_instances associated with a location_id
    argument passed in is an int for the location id
"""


def box_plot(loc_id):
    out_b = stop_instance.objects.filter(door=1, location_distance__isnull=False, location_id=loc_id).values_list(
        'location_distance', flat=True)
    out_list = list(out_b)
    meter_to_foot = Decimal(.3048)
    loc_dist_meters = [i * meter_to_foot for i in out_list]
    fig = go.Figure()
    fig.add_trace(go.Box(x=loc_dist_meters, name='location_distance_dist'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='Box Plot ' + str(loc_id),
        xaxis_title='location_distance in meters',
        yaxis_title='location_id',
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div


"""
    Returns a div object that contains a plotly bar chart
    bar chart displays number of in bounds/ out of bounds stops
    by day of week
    argument passed in is an int for the location id
"""


def bar_chart_week(loc_id):
    out_b = stop_instance.objects.annotate(weekday=ExtractWeekDay('service_date')).values('weekday').annotate(count=Count('weekday')).values('weekday', 'count').filter(door=1, location_distance__gt=out_of_bounds, location_id=loc_id)
    o_y = [i['count'] for i in out_b.iterator()]
    in_b = stop_instance.objects.annotate(weekday=ExtractWeekDay('service_date')).values('weekday').annotate(count=Count('weekday')).values('weekday', 'count').filter(door=1, location_distance__lte=out_of_bounds, location_id=loc_id)
    in_y = [i['count'] for i in in_b.iterator()]
    days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    fig = go.Figure()
    fig.add_trace(go.Bar(x=days, y=o_y, name='out of bounds stops'))
    fig.add_trace(go.Bar(x=days, y=in_y, name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='Out of bound vs in bound stops by day of week ' + str(loc_id),
        xaxis_title='day of week',
        yaxis_title='number of stop instances',
        barmode='overlay'
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div


"""
    Returns a div object that contains a plotly bar chart
    bar chart displays number of in bounds/ out of bounds stops
    by month
    argument passed in is an int for the location id
"""


def bar_chart_month(loc_id):
    out_b = stop_instance.objects.annotate(month=ExtractMonth('service_date')).values('month').annotate(count=Count('month')).values('month', 'count').filter(door=1, location_distance__gt=out_of_bounds, location_id=loc_id)
    o_y = [i['count'] for i in out_b.iterator()]
    in_b = stop_instance.objects.annotate(month=ExtractMonth('service_date')).values('month').annotate(count=Count('month')).values('month', 'count').filter(door=1, location_distance__lte=out_of_bounds, location_id=loc_id)
    in_y = [i['count'] for i in in_b.iterator()]
    month = ['Jan', 'Feb', 'Mar', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig = go.Figure()
    fig.add_trace(go.Bar(x=month, y=o_y, name='out of bounds stops'))
    fig.add_trace(go.Bar(x=month, y=in_y, name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='Out of bound vs in bound stops by month ' + str(loc_id),
        xaxis_title='month',
        yaxis_title='number of stop instances',
        barmode='overlay'
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div

