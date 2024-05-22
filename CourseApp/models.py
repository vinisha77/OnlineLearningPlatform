# CourseApp/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Course(models.Model):
    author = models.CharField(max_length=100, default='Unknown Author')
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
