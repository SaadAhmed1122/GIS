# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Banks

# # # Create your views here.
# # def index (request):
# #     return render (request, 'templates/testdb/index.html')
# def say_hello(request):
#     return render(request, 'index.html')
# def index (request):
# #Access all rows of banks table
#     banks = Banks.objects.all()
#     return render (request, 'testdb/index.html', {'banks': banks})
from django.shortcuts import render, redirect  
from testdb.forms import EmployeeForm
from testdb.models import Employee  

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  # add indentation here
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})
  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
def add_business(request):
    # your view logic here
    return render(request, 'add_business.html')