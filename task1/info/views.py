from django.shortcuts import get_object_or_404, redirect, render
from info.models import *
from info.views import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

# Create your views here.
def employees(request):
    return render(request,'employees.html')

def login_page(request):
    

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username ")
            return redirect('/login/')
        
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            print("User authenticated successfully:", user.username)
            login(request, user)
            return redirect('/employees/')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/login/')

    return render(request, 'login.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        
        user=User.objects.create(
            first_name= first_name,
            last_name = last_name,
            email = email,
            username = username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully!")
        
        return redirect('/register/')

    return render(request, 'register.html')

def add_employee(request):
    
    if request.method=="POST":
        data=request.POST

        e_name=data.get('e_name')
        e_addr=data.get('e_addr')

        Employee.objects.create(
            e_name=e_name,
            e_addr=e_addr,
        )
        messages.info(request, "Employee added Successfully!")
        return redirect('/employees/')
    
def employee_list(request):
    queryset = Employee.objects.all()
    context={'employees':queryset}
    return render(request, 'employee_list.html',context)

def delete_emp(request,id):
    queryset=Employee.objects.get(e_id=id)
    queryset.delete()
    return redirect('employee_list')

def update_emp(request,id):
    queryset=Employee.objects.get(e_id=id)
    if request.method == "POST":
        data=request.POST
        e_name=data.get('e_name')
        e_addr=data.get('e_addr')

        queryset.e_name=e_name
        queryset.e_addr=e_addr
        
        queryset.save()
        messages.info(request, "Employee Updated Successfully!")
    context={'employees':queryset}
    return render(request, 'update_emp.html',context)

def add_department(request):
    
    if request.method == "POST":
        data = request.POST

        d_name = data.get('d_name')
        manager_name = data.get('manager')

        # Fetch the Employee instance based on the provided manager name
        manager_employee = get_object_or_404(Employee, e_name=manager_name)

        Department.objects.create(
            d_name=d_name,
            manager=manager_employee,
        )
        messages.info(request, "Department added Successfully!")
        return redirect('/employees/')
    
def department_list(request):
    queryset = Department.objects.all()
    context={'departments':queryset}
    return render(request, 'department_list.html',context)


def update_dep(request,id):
    queryset=Department.objects.get(d_id=id)
    if request.method == "POST":
        data=request.POST
        d_name=data.get('d_name')
        manager=data.get('manager')

        manager_employee = get_object_or_404(Employee, e_name=manager)


        queryset.d_name=d_name
        queryset.manager=manager_employee
        
        queryset.save()
        messages.info(request, "Department Updated Successfully!")
    context={'departments':queryset}
    return render(request, 'update_dep.html',context)

def delete_dep(request,id):
    queryset=Department.objects.get(d_id=id)
    queryset.delete()
    return redirect('department_list')
