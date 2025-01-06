# projects/models.py

from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
