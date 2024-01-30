from django.shortcuts import render, redirect  
from testdb.forms import RoadForm
from testdb.models import RoadData  
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
def add_business(request):
    # your view logic here
    return render(request, 'add_business.html')