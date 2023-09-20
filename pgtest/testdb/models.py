from django.db import models
# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    lat = models.DecimalField(max_digits=19, decimal_places=10)
    lng = models.DecimalField(max_digits=19, decimal_places=10) 
    class Meta:  
        db_table = "employee" 

        
class Banks(models.Model):
    gid = models.AutoField(primary_key=True)
    code = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'banks' 
