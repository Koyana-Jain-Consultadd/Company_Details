from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def login_page(request):
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