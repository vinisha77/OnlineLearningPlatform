# Generated by Django 5.0.4 on 2024-05-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=100),
        ),
    ]