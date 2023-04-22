from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project.serializer import ProjectSerializer,EmployeeWorkProjectSerializer
from project.models import Project, Supervisor, EmployeeWorkProject
from employee.models import Employee
from department.models import Deparment

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self,request,*args,**kwargs):
        project_data = request.data
        employee = Employee.objects.get(id=project_data["supervisor"]["employee_id"])
        
        new_sup = Supervisor.objects.create(employee_id=employee,workload=project_data["supervisor"]["workload"])
        new_sup.save()
        department = Deparment.objects.get(id=project_data["department_id"])
        new_project = Project.objects.create(supervisor=new_sup,department_id=department,name=project_data["name"],total_hours_to_complete=project_data["total_hours_to_complete"],total_hours_completed=project_data["total_hours_completed"])
        new_project.save()

        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)
    

class EmployeeWorkProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeWorkProject.objects.all()
    serializer_class = EmployeeWorkProjectSerializer

    # def create(self,request,*args,**kwargs):
    #     project_data = request.data
    #     breakpoint()
    #     employee = Employee.objects.get(id=project_data["supervisor"]["employee_id"])
        
    #     new_sup = Supervisor.objects.create(employee_id=employee,workload=project_data["supervisor"]["workload"])
    #     new_sup.save()
    #     department = Deparment.objects.get(id=project_data["department_id"])
    #     new_project = Project.objects.create(supervisor=new_sup,department_id=department,name=project_data["name"],total_hours_to_complete=project_data["total_hours_to_complete"],total_hours_completed=project_data["total_hours_completed"])
    #     new_project.save()

    #     serializer = ProjectSerializer(new_project)
    #     return Response(serializer.data)