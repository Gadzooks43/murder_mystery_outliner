# projects/models.py

from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    characters = models.ManyToManyField('Character', blank=True)
    plot_a = models.ForeignKey('APlot', on_delete=models.CASCADE, related_name='a_plots', null=True, blank=True)
    plot_b = models.ForeignKey('BPlot', on_delete=models.CASCADE, related_name='b_plots', null=True, blank=True)
    plot_c = models.ForeignKey('CPlot', on_delete=models.CASCADE, related_name='c_plots', null=True, blank=True)
    chapters = models.ManyToManyField('Chapter', blank=True)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=200)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default="")
    background = models.TextField(default="")
    alibi = models.TextField(default="")
    secrets = models.TextField(default="")
    motive = models.TextField(default="")

    def __str__(self):
        return self.name

class Plot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='plots')
    characters = models.ManyToManyField(Character, blank=True)

    def __str__(self):
        return self.title

class APlot(Plot):
    murder = models.TextField(default="")  # Specific to APlot
    archetype = models.ForeignKey('Archetype', on_delete=models.CASCADE, null=True, blank=True)
    cause_of_death = models.ForeignKey('CauseOfDeath', on_delete=models.CASCADE, null=True, blank=True)
    red_herrings = models.TextField(default="")  # Specific to APlot

class BPlot(Plot):
    connection_to_a_plot = models.TextField(default="")

class CPlot(Plot):
    connection_to_a_plot = models.TextField(default="")
    connection_to_b_plot = models.TextField(default="")

class Chapter(models.Model):
    description = models.TextField(default="")
    number = models.IntegerField(null=False, blank=False)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return f"Chapter {self.number}: {self.description[:50]}..."
    

class Archetype(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    examples = models.TextField(default="")
    
    def __str__(self):
        return self.name

class CauseOfDeath(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    
    def __str__(self):
        return self.name
    
class Motives(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    
    def __str__(self):
        return self.name