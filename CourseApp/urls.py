from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # View for listing courses
    path('create/', views.create_course, name='create_course'),
    path('<int:pk>/edit/', views.edit_course, name='edit_course'),
    path('<int:pk>/delete/', views.delete_course, name='delete_course'),
]
