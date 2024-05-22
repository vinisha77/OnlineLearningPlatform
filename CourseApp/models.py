# CourseApp/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('security', 'Security'),
        # Add more categories as needed
    ]
    
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True, default='default_course_image.jpg')
    author = models.CharField(max_length=100, default='Unknown Author')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='programming')
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')

    def __str__(self):
        return self.title
