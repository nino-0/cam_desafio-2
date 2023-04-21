from django.contrib import admin

from project.models import Project

class Projects(admin.ModelAdmin):
    list_display = ['id','name','total_hours_to_complete','total_hours_completed','estimated_date']
    list_display_links = ['name','total_hours_to_complete','total_hours_completed','estimated_date']
    search_fields=['name','id']

admin.site.register(Project,Projects)
