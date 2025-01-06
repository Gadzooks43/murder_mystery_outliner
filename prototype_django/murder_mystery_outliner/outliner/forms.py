# projects/forms.py

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']  # We only need 'name' from user for now
