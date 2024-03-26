from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    technology = models.CharField(max_length = 100, default = '')
    image = models.ImageField(upload_to='photos/projects')
    
    def __str__(self) -> str:
        return self.name
    


class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    value = models.IntegerField(choices=[(i, i) for i in range(1, 8)])  
    created_at = models.DateTimeField(auto_now_add=True)
