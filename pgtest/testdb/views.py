from django.shortcuts import render, redirect  
from testdb.forms import RoadForm
from testdb.models import RoadData  
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RoadData, Sign, Inspection
from django.contrib.gis.geos import GEOSGeometry
from .forms import RoadForm
from .models import Road

@login_required
def emp(request):  
    if request.method == "POST":
        form = RoadForm(request.POST, request.FILES, user=request.user)
        print(form)
        if form.is_valid():  
            try:
                print(request.FILES)
                form.save()
                return redirect('/show')  
            except:  
                pass  
    else:  # add indentation here
        form = RoadForm(user=request.user)  
    return render(request,'index.html',{'form':form})
  
def show(request):  
    roads_data = RoadData.objects.all()
    print(roads_data)  
    return render(request,"show.html",{'roads_data':roads_data})  
def edit(request, id):  
    road_data = RoadData.objects.get(id=id)  
    return render(request,'edit.html', {'road_data':road_data})  
def update(request, id):  
    road_data = RoadData.objects.get(id=id)  
    form = RoadForm(request.POST, instance = road_data)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'road_data': road_data})  
def destroy(request, id):  
    road_data = RoadData.objects.get(id=id)  
    road_data.delete()  
    return redirect("/show")
def road_create(request):
    if request.method == 'POST':
        form = RoadForm(request.POST, request.FILES)
        if form.is_valid():
            road = form.save(commit=False)
            # Convert the geometry from WKT to GeoJSON
            geometry = GEOSGeometry(road.geometry.wkt)
            road.geometry = geometry

            road.save()

            return redirect('road_list')
    else:
        form = RoadForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)

def road_list(request):
    roads = Road.objects.all()

    context = {
        'roads': roads
    }

    return render(request, 'show.html', context)

  
# def import_data(request):
#     if request.method == 'POST':
#         form = RoadImportForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Import data and update the road registry
#             pass
#     else:
#         form = RoadImportForm()
#     return render(request, 'import_data.html', {'form': form})

# def export_data(request):
#     if request.method == 'POST':
#         form = RoadExportForm(request.POST)
#         if form.is_valid():
#             # Export data in the selected format
#             pass
#     else:
#         form = RoadExportForm()
#     return render(request, 'export_data.html', {'form': form})

# def update_road(request, id):
#     # Update the road graph and attributes
#     pass

# def query_data(request):
#     if request.method == 'POST':
#         form = QueryForm(request.POST)
#         if form.is_valid():
#             # Perform the query and return the results
#             pass
#     else:
#         form = QueryForm()
#     return render(request, 'query_data.html', {'form': form})
def road_form_view(request):
    if request.method == 'POST':
        form = RoadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RoadForm()
    return render(request, 'road_form.html', {'form': form})
