from django.contrib import admin
from .models import Road
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
admin.site.site_url = "show"

class RoadAdmin(LeafletGeoAdmin):
    list_display=('road_name', 'road_type','start_measure','end_measure','geometry')
    
    def save_model(self, request, obj, form, change):
        print("Geometry data:", obj.geometry)
        super().save_model(request, obj, form, change)
        
    
admin.site.register(Road, RoadAdmin)