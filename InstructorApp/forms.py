from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from CourseApp.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'image', 'category', 'difficulty_level', 'author']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('description', css_class='form-control'),
            Field('price'),
            Field('image'),
            Field('category'),
            Field('difficulty_level'),
            Field('author')
        )
