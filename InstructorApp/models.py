from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    #profile_picture = models.ImageField(upload_to='instructor_profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username