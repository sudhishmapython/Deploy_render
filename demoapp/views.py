from django.http import HttpResponse
from django.shortcuts import render, redirect

from demoapp.forms import ProductForm, EmployeeForm
from demoapp.models import Product, Student, Employee, College


# Create your views here.


def fun1(request):
    return render(request, 'index.html')


def add_form(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e_read')
    return render(request, 'demo.html', {'form': form})


def read_form(request):
    data = Product.objects.all()
    return render(request, 'demo_read.html', {'data': data})


def update_form(request, id):
    data = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = ProductForm(instance=data)
    return render(request, 'edit.html', {'form': form})


def stud_add(request):
    if request.method == 'POST':
        name = request.POST['f_name']
        roll_no = request.POST['r_no']
        mark = request.POST['m_mark']
        stud = Student(name=name, roll_no=roll_no, mark=mark)
        stud.save()
    return render(request, 'stud_add.html')


def emp_add(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e_read')
    return render(request, 'emp_add.html', {'form': form})


def emp_read(request):
    data = Employee.objects.all()
    return render(request, 'emp_read.html', {'data': data})


def emp_update(request, id):
    data = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('e_read')

    else:
        form = EmployeeForm(instance=data)

    return render(request, 'emp_edit.html', {'form': form})


def demo_html(request):
    return render(request, 'demo_html.html')



def college_add(request):
    if request.method == 'POST':
        name = request.POST['cname']
        place = request.POST['cplace']
        phone = request.POST['cphone']
        clg=College(name=name,place=place,phno=phone)
        clg.save()

    return render(request, 'demo_html.html')