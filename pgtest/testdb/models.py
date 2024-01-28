from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoadData(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add user field
    etype = models.CharField(max_length=255)  # Assuming 'etype' is the type field
    edescription = models.TextField()  # Assuming 'edescription' is the description field
    lat = models.DecimalField(max_digits=19, decimal_places=10)
    lng = models.DecimalField(max_digits=19, decimal_places=10)
    image = models.ImageField(upload_to='road_defect_images/', null=True, blank=True)
    image_filename = models.CharField(max_length=255, null=True, blank=True)

    class Meta:  
        db_table = "road_data"