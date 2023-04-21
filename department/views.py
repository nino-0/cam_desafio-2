from django.shortcuts import render

from rest_framework import viewsets
from department.models import Deparment
from department.serializer import DepartmentSerializer

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Deparment.objects.all()
    serializer_class = DepartmentSerializer
