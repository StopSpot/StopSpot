from SysMap.models import stop_instance
import plotly.offline as py
import plotly.graph_objs as go
from decimal import Decimal

from django.db.models import Count
out_of_bounds = 98.4252 #in feet


def bar_chart_routes():
    out_b = stop_instance.objects.values('route_number').annotate(count=Count('route_number')).values('route_number', 'count').filter(door=1, route_number__isnull=False, location_distance__gt=out_of_bounds)
    o_x = [str(i['route_number']) for i in out_b.iterator()]
    o_y = [i['count'] for i in out_b.iterator()]
    in_b = stop_instance.objects.values('route_number').annotate(count=Count('route_number')).values('route_number', 'count').filter(door=1, route_number__isnull=False, location_distance__lte=out_of_bounds)
    in_x = [str(i['route_number']) for i in in_b.iterator()]
    in_y = [i['count'] for i in in_b.iterator()]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=o_x, y=o_y, name='out of bounds stops'))
    fig.add_trace(go.Bar(x=in_x, y=in_y, name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='Out of bound vs in bound stops by route ',
        xaxis_title='route number',
        xaxis_type='category',
        yaxis_title='number of stop instances',
        margin=dict(
            l=20,
            r=20,
            b=80,
            t=80,
            pad=2),
        width=1000,
        height=700,
        uniformtext_minsize=8, uniformtext_mode='hide',
        xaxis_tickangle=60
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div


def bar_chart_stops_on_route(route):
    out_b = stop_instance.objects.values('location_id').annotate(count=Count('location_id')).values('location_id', 'count').filter(door=1,
                                                                                                               location_distance__gt=out_of_bounds,
                                                                                                               route_number=route)
    o_x = [i['location_id'] for i in out_b.iterator()]
    o_y = [i['count'] for i in out_b.iterator()]
    in_b = stop_instance.objects.values('location_id').annotate(count=Count('location_id')).values('location_id', 'count').filter(door=1,
                                                                                                              location_distance__lte=out_of_bounds,
                                                                                                              route_number=route)
    in_x = [i['location_id'] for i in in_b.iterator()]
    in_y = [i['count'] for i in in_b.iterator()]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=o_x, y=o_y, name='out of bounds stops'))
    fig.add_trace(go.Bar(x=in_x, y=in_y, name='in bounds stops'))
    fig.update_traces(opacity=.50)
    fig.update_layout(
        title='Out of bound vs in bound stops by route ' + str(route),
        xaxis_title='location id',
        yaxis_title='number of stop instances',
        uniformtext_minsize=8, uniformtext_mode='hide',
        xaxis_tickangle=60,
        xaxis_type='category',
        margin=dict(
            l=20,
            r=20,
            b=80,
            t=80,
            pad=2),
        width=1000,
        height=700,
    )

    plot_div = py.plot(fig, output_type='div')
    return plot_div