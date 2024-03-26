from django.shortcuts import render
from .models import Skill
# Create your views here.
def skill(request):
    skills = Skill.objects.all()
    return render(request,'skill/skills.html',{'skills':skills})
