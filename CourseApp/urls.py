from django.urls import path
from . import views  # Assuming your views are in the same app directory

urlpatterns = [
    # Existing URL patterns for your app (if any)
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('search/', views.search_courses, name='search_courses'),
]
