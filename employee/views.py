from django.shortcuts import render
from rest_framework import viewsets
from employee.serializer import EmployeeSerializer
from employee.models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer