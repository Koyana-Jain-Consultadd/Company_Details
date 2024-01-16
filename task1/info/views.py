from django.shortcuts import redirect, render
from .models import *
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