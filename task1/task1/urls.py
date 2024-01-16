"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from info.views import *
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('register/' ,register, name="register"),
    path('login/' ,login_page, name="login_page"),
    path('employees/', employees, name="employees"),
    path('add_employee/', add_employee, name="add_employee"),
    path('employee_list/', employee_list, name="employee_list"),
    path('delete_emp/<id>/', delete_emp, name="delete_emp"),
    path('update_emp/<id>/', update_emp, name="update_emp"),
    path('add_department/', add_department, name="add_department"),
    path('department_list/', department_list , name="department_list"),
    path('update_dep/<id>/', update_dep, name="update_dep"),
    path('delete_dep/<id>/', delete_dep, name="delete_dep"),
    
]
