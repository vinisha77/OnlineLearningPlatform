# CourseApp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course

class CourseFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'All Categories'),
        ('programming', 'Programming'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('security', 'Security'),
        ('cyber_security', 'Cyber Security'),
        ('blockchain', 'Blockchain'),
        ('big_data', 'Big Data'),
        ('iot', 'Internet of Things (IoT)'),
        ('robotics', 'Robotics'),
        ('software_testing', 'Software Testing'),
        ('business_analysis', 'Business Analysis'),
        ('project_management', 'Project Management'),
        ('digital_marketing', 'Digital Marketing'),
        ('seo', 'Search Engine Optimization (SEO)'),
        ('content_creation', 'Content Creation'),
        ('graphic_design', 'Graphic Design'),
        ('ux_ui', 'UX/UI Design'),
        ('animation', 'Animation'),
        ('video_editing', 'Video Editing'),
        ('music_production', 'Music Production'),
        ('finance', 'Finance'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('leadership', 'Leadership'),
        ('personal_development', 'Personal Develop')
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

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'difficulty_level', 'price', 'image']

