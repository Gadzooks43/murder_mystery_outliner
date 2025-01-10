# projects/models.py

from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='plots')

    def __str__(self):
        return self.title

class APlot(Plot):
    pass

class BPlot(Plot):
    pass

class CPlot(Plot):
    pass

class Chapter(models.Model):
    description = models.TextField()
    number = models.IntegerField()
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return f"Chapter {self.number}: {self.description[:50]}..."
    

class Archetype(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    examples = models.TextField()
    
    def __str__(self):
        return self.name

class CauseOfDeath(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Motives(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name