from django.contrib import admin
from .models import Skill
# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ['technology','proficiency']
        
        
admin.site.register(Skill,SkillAdmin)
