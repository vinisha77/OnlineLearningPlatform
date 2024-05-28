from django import forms
from CourseApp.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'image', 'category', 'difficulty_level', 'author']