from django.db import models

# Create your models here.
class Skill(models.Model):
    technology =models.CharField(max_length = 30)
    proficiency = models.IntegerField()
