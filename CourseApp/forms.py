# CourseApp/forms.py
from django import forms

class CourseFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'All Categories'),
        ('programming', 'Programming'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('security', 'Security'),
        # Add more categories as needed
    ]
    
    DIFFICULTY_CHOICES = [
        ('', 'All Levels'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    difficulty_level = forms.ChoiceField(choices=DIFFICULTY_CHOICES, required=False)
    min_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10)
    max_price = forms.DecimalField(required=False, decimal_places=2, max_digits=10)
