from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from CourseApp.models import Course  

class Level(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'personalpath_level'
        
    def __str__(self):
        return self.name

class PersonalizedLearningPath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.level.name}"
