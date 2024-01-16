from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=150)
    e_addr = models.CharField(max_length=500)


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length = 255)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
