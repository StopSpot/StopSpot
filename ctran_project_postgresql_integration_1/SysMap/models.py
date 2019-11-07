from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class stop_instance(models.Model):
    id = models.AutoField(primary_key=True)
    service_date = models.DateField(null=True)
    vehicle_number = models.IntegerField(null=True, default=-1)
    leave_time = models.IntegerField(null=True, default=-1)
    train = models.IntegerField(null=True, default=-1)
    badge = models.IntegerField(null=True, default=-1)
    route_number = models.IntegerField(null=True, default=-1)
    direction = models.IntegerField(null=True, default=-1)
    service_key = models.CharField(null=True, max_length=1)
    trip_number = models.IntegerField(null=True, default=-1)
    stop_time = models.IntegerField(null=True, default=-1)
    arrive_time = models.IntegerField(null=True, default=-1)
    dwell = models.IntegerField(null=True, default=-1)
    location_id = models.IntegerField(null=True, default=-1)
    door = models.IntegerField(null=True, default=-1)
    lift = models.IntegerField(default=-1, null=True )
    ons = models.IntegerField(null=True, default=-1)
    offs = models.IntegerField(null=True, default=-1)
    estimated_load = models.IntegerField(null=True, default=-1)
    maximum_speed = models.IntegerField(null=True, default=-1)
    train_mileage = models.DecimalField(null=True, max_digits=11, decimal_places=5)
    pattern_distance = models.DecimalField(null=True, max_digits=11, decimal_places=5)
    location_distance = models.DecimalField(null=True, max_digits=11, decimal_places=5)
    x_coordinate = models.DecimalField(null=True, default=-1, max_digits=11, decimal_places=7)
    y_coordinate = models.DecimalField(null=True, default=-1, max_digits=11, decimal_places=7)
    data_source = models.IntegerField(null=True, default=-1)
    schedule_status = models.IntegerField(null=True, default=-1)
    trip_id = models.IntegerField(null=True, default=-1)


class bus_stop(models.Model):
    stop_id= models.IntegerField(primary_key=True,default=-1)
    stop_code= models.IntegerField(default=-1, null=True)
    stop_name= models.CharField(max_length=100,default='none provided',null=True)
    stop_desc= models.CharField(max_length=100,default='none provided',null=True)
    stop_lat= models.DecimalField(max_digits=11,decimal_places=8)
    stop_lon= models.DecimalField(max_digits=11,decimal_places=8)
    zone_id= models.IntegerField(default=-1,null=True)
    stop_url= models.CharField(max_length=100,default='none provided',null=True)
    location_type= models.IntegerField(default=-1)
    parent_station= models.CharField(max_length=100,default='none provided',null=True)
    stop_timezone= models.CharField(max_length=100,default='none provided',null=True)
    wheelchair_boarding= models.IntegerField(default=-1,null=True)

    class Meta:
        verbose_name_plural = 'bus_stops'


