from rest_framework import serializers
from department.models import Deparment

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deparment
        fields = '__all__'