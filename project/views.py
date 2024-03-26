from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Rating
from .forms import RatingForm
from django.db.models import Avg

# Create your views here.
def project(request):
    projects = Project.objects.annotate(avg_rating=Avg('ratings__value')).order_by('-avg_rating')
    return render(request,'project/projects.html',{'projects':projects})

def project_detail(request,project_id):
    project = Project.objects.get(id=project_id)
    ratings = Rating.objects.filter(project = project)
    average_rating = ratings.aggregate(Avg('value'))['value__avg'] or 0
    return render(request,'project/project_detail.html',{'project':project, 'average_rating':average_rating})




def rating(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        print('form is not valid')
        if form.is_valid():
            print('form is valid')
            rating = form.save(commit=False)
            rating.project = project
            rating.user = request.user  
            rating.save()
            messages.success(request, 'Rating submitted successfully.')
            return redirect('project_detail', project_id=project_id)
    else:
        form = RatingForm()
    return render(request, 'project/projects.html', {'form': form})


