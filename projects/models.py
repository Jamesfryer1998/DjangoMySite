from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/media/')
    git_repo = models.URLField(max_length=200, blank=True)