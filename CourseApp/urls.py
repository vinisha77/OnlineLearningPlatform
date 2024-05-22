from django.urls import path
from . import views  # Assuming your views are in the same app directory

urlpatterns = [
    # Existing URL patterns for your app (if any)
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
