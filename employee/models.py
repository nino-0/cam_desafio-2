from django.db import models
from department.models import Deparment

class Employee(models.Model):
  name = models.CharField(max_length=150,unique=True)
  cpf = models.CharField(max_length=11,unique=True)  
  rg = models.CharField(max_length=13,unique=True)
  gender = models.CharField(max_length=1)
  has_a_license = models.BooleanField(default=False)
  wage_value = models.FloatField(default=0)
  weekly_workload = models.FloatField(default=0)
  department_id = models.ForeignKey(Deparment, on_delete=models.CASCADE)

  def __str__(self):
    return self.name+" "+self.cpf

  class Meta:
    ordering = ["name"]
    
