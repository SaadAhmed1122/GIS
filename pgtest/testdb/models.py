from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


# Create your models here.
class RoadData(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add user field
    etype = models.CharField(max_length=255)  # Assuming 'etype' is the type field
    edescription = models.TextField()  # Assuming 'edescription' is the description field
    lat = models.DecimalField(max_digits=19, decimal_places=10)
    lng = models.DecimalField(max_digits=19, decimal_places=10)
    image = models.ImageField(upload_to='road_defect_images/', null=True, blank=True)
    image_filename = models.CharField(max_length=255, null=True, blank=True)
    geometry = models.LineStringField(srid=4326, default='SRID=4326;LINESTRING(0 0, 1 1)')


    class Meta:  
        db_table = "road_data"    
        
class RoadDefectType(models.TextChoices):
    POTHOLE = 'Pothole', 'Pothole'
    CRACK = 'Crack', 'Crack'
    SINKHOLE = 'Sinkhole', 'Sinkhole'
    SURFACE_EROSION = 'Surface Erosion', 'Surface Erosion'
    OTHER = 'Other', 'Other'

class Road(models.Model):
    road_id = models.AutoField(primary_key=True)
    road_name = models.CharField(max_length=255)
    road_type = models.CharField(max_length=50)
    start_measure = models.FloatField()
    end_measure = models.FloatField()
    geometry = models.LineStringField(srid=4326)
class RoadHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    updated_by_user = models.ForeignKey('User', on_delete=models.CASCADE)
    update_date = models.DateTimeField()
    graph_changes = models.JSONField()
    attribute_changes = models.JSONField()

class Sign(models.Model):
    sign_id = models.AutoField(primary_key=True)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    sign_type = models.CharField(max_length=50)
    installation_date = models.DateField()
    expiry_date = models.DateField()

class Inspection(models.Model):
    inspection_id = models.AutoField(primary_key=True)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    inspector = models.ForeignKey('User', on_delete=models.CASCADE)
    inspection_date = models.DateField()
    surface_malformations = models.JSONField()
    sign_damages = models.JSONField()
    safety_device_damages = models.JSONField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=50)

class Query(models.Model):
    query_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_date = models.DateTimeField()
    query_type = models.CharField(max_length=50)
    query_details = models.JSONField()
    results = models.JSONField()
    road_defect_type = models.CharField(max_length=20, choices=RoadDefectType.choices)
