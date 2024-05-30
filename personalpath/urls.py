# personalpath/urls.py
from django.urls import path
from personalpath import views as personal  # Import the views from UserApp

urlpatterns = [
    path('select-course/', personal.select_course, name='select_course'),
    path('select-level/', personal.select_level, name='select_level'),
    path('learning-path/<int:path_id>/', personal.view_learning_path, name='view_learning_path'),
]
