from django.contrib import admin
from department.models import Deparment

class Departaments(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['name']
    search_fields=['name',]

admin.site.register(Deparment,Departaments)
