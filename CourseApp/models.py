# CourseApp/models.py
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('security', 'Security'),
         ('cyber_security', 'Cyber Security'),
        ('blockchain', 'Blockchain'),
        ('big_data', 'Big Data'),
        ('iot', 'Internet of Things (IoT)'),
        ('robotics', 'Robotics'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('leadership', 'Leadership'),
        ('finance', 'Finance'),
        ('entrepreneurship', 'Entrepreneurship'),
        
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
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'
