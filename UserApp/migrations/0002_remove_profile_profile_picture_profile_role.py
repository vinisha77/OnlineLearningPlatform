# Generated by Django 5.0.4 on 2024-05-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default='user', max_length=20),
            preserve_default=False,
        ),
    ]
