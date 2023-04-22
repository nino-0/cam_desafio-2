from django.db import models
from department.models import Deparment
from employee.models import Employee
import datetime


class Supervisor(models.Model):    
    employee_id = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    workload = models.FloatField(default=0)

class EmployeeWorkProject(models.Model): 
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    workload = models.FloatField(default=0)
    class Meta:
      unique_together = ('employee',)
class Project(models.Model):
  department_id = models.ForeignKey(Deparment, on_delete=models.CASCADE)
  name = models.CharField(max_length=150)
  total_hours_to_complete = models.FloatField(default=0)
  total_hours_completed = models.FloatField(default=0)
  estimated_date = models.DateField(null=True)
  last_measurement = models.DateField(default=datetime.date.today)
  supervisor = models.OneToOneField(Supervisor, on_delete=models.CASCADE)
  work_group = models.ManyToManyField(EmployeeWorkProject)
  class Meta:
    unique_together = ('name', 'department_id',)
  def __str__(self) -> str:
      return self.name
  
