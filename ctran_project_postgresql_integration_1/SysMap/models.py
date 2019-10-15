from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class stop_instance(models.Model):
    service_date= models.DateField()
    vehicle_number= models.IntegerField()
    leave_time= models.IntegerField()
    train= models.IntegerField()
    badge: models.IntegerField()
    route_number: models.IntegerField()
    direction: models.IntegerField()
    service_key: models.CharField(max_length=10)
    trip_number: models.IntegerField()
    stop_time: models.IntegerField()
    arrive_time: models.IntegerField()
    dwell: models.IntegerField()
    location_id: models.IntegerField()
    door: models.IntegerField()
    life: models.IntegerField()
    ons: models.IntegerField()
    offs: models.IntegerField()
    estimated_load: models.IntegerField()
    maximum_speed: models.IntegerField()
    train_mileage: models.DecimalField(max_digits=7,decimal_places=7)
    pattern_distance: models.DecimalField(max_digits=7,decimal_places=7)
    location_distance: models.DecimalField(max_digits=7,decimal_places=7)
    x_coordinate: models.DecimalField(max_digits=7,decimal_places=7)
    y_coordinate: models.DecimalField(max_digits=7,decimal_places=7)
    data_source: models.IntegerField()
    schedule_status: models.IntegerField()
    trip_id: models.IntegerField()


class bus_stop(models.Model):
    stop_id= models.IntegerField(primary_key=True,default=-1)
    stop_code= models.IntegerField(default=-1)
    stop_name= models.CharField(max_length=100,default='none provided')
    stop_desc= models.CharField(max_length=100,default='none provided')
    stop_lat= models.DecimalField(max_digits=11,decimal_places=8)
    stop_lon= models.DecimalField(max_digits=11,decimal_places=8)
    zone_id= models.IntegerField(default=-1)
    stop_url= models.CharField(max_length=100,default='none provided')
    location_type= models.IntegerField(default=-1)
    parent_station= models.CharField(max_length=100,default='none provided')
    stop_timezone= models.CharField(max_length=100,default='none provided')
    wheelchair_boarding= models.IntegerField(default=-1)

    class Meta:
        verbose_name_plural = 'bus_stops'


