from django.contrib import admin

from project.models import Project,EmployeeWorkProject,Supervisor

class Supervisors(admin.ModelAdmin):
    list_display = ['id','employee_id','workload']
    list_display_links = ['id','employee_id','workload']
    search_fields=['id','employee_id']
class Projects(admin.ModelAdmin):
    list_display = ['id','name','total_hours_to_complete','total_hours_completed','estimated_date']
    list_display_links = ['name','total_hours_to_complete','total_hours_completed','estimated_date']
    search_fields=['name','id']

class EmployeesWorkProjects(admin.ModelAdmin):
    list_display = ['id','employee','workload']
    list_display_links = ['id','employee','workload']
    search_fields=['id','employee']

admin.site.register(Project,Projects)
admin.site.register(EmployeeWorkProject,EmployeesWorkProjects)
admin.site.register(Supervisor,Supervisors)
