

# Register your models here.
from django.contrib import admin
from .models import Project, Rating

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','title','technology',)  

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'value', 'created_at')  
