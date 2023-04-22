from rest_framework import serializers
from project.models import Project,EmployeeWorkProject

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
      model = Project
      fields = '__all__'
      depth = 2

class EmployeeWorkProjectSerializer(serializers.ModelSerializer):
    class Meta:
      model = EmployeeWorkProject
      fields = '__all__'
      depth = 1     