from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from project.serializer import ProjectSerializer
from project.models import Project
from project.models import Supervisor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self,request,*args,**kwargs):
        project_data = request.data
        new_sup = Supervisor.objects.create(employee_id=project_data["supervisor"]["employee_id"],workload=project_data["supervisor"]["workload"])
        new_sup.save()

        new_project = Project.objects.create(supervisor=new_sup,department_id=project_data["department_id"],name=project_data["name"],total_hours_to_complete=project_data["total_hours_to_complete"],total_hours_completed=project_data["total_hours_completed"])
        new_project.save()

        serializer = ProjectSerializer(new_project)
        return Response(serializer)