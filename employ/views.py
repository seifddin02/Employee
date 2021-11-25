from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import EmployeeForm
from .filters import EmployeeFilter
# Create your views here.


def home(request):
    employees = Employee.objects.all()

    myFilter = EmployeeFilter(request.GET, queryset= employees)
    employees = myFilter.qs


    context = {'employees' :employees, 'myFilter' :myFilter}

    return render(request, 'employ/dashboard.html', context)

def employee(request, pk):

    employee = Employee.objects.get(id=pk)

    context = {'employee': employee}

    return render(request, 'employ/employee.html', context)

def addEmployee(request):

    form = EmployeeForm()
    if request.method == 'POST':
        #print(request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'employ/employee_form.html', context)

def updateEmployee(request, pk):

    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'employ/employee_form.html', context)

def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('/')
    context = {'person':employee}
    return render(request, 'employ/delete_employee.html', context)