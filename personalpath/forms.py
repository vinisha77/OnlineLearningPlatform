from django import forms
from CourseApp.models import Course  # Importing Course model from Course app
from .models import Level

class CourseSelectionForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.RadioSelect)

class LevelSelectionForm(forms.Form):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    level = forms.ChoiceField(choices=LEVEL_CHOICES, label='Select Level')

