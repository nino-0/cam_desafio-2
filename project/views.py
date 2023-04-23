from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project.serializer import ProjectSerializer,EmployeeWorkProjectSerializer
from project.models import Project, Supervisor, EmployeeWorkProject
from employee.models import Employee
from department.models import Deparment
from django.db.models import Avg, Count, Min, Sum


def can_add_employee(employee_id,new_workload):
    employee = Employee.objects.get(id=employee_id)
    hours_work = EmployeeWorkProject.objects.filter(employee=employee_id).aggregate(Sum('workload'))
    hours_super = Supervisor.objects.filter(employee_id=employee_id).aggregate(Sum('workload'))
    total_emp_work =  (hours_super['workload__sum'])+(hours_work['workload__sum'])
    if total_emp_work + new_workload <= employee.weekly_workload:
        return True
    return False
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

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            project = Project.objects.get(id=data['project_id'])
            employee = Employee.objects.get(id=data['employee_id'])
            workload = data['workload']
            
            if not can_add_employee(employee.id,workload):
                raise 'not allowed.'
            
            empWorkPro = EmployeeWorkProject.objects.create(project=project,employee=employee,workload=workload)
            empWorkPro.save()
            return Response(EmployeeWorkProjectSerializer(empWorkPro).data)
        except Exception as e:
            return Response(data=[],status=400)
        