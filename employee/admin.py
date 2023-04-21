from django.contrib import admin
from employee.models import Employee

class Employees(admin.ModelAdmin):
    list_display = ['id','name','gender','cpf','department_id']
    list_display_links = ['name','gender','cpf','department_id']
    search_fields=['id','name','gender','cpf','department_id']

admin.site.register(Employee,Employees)
