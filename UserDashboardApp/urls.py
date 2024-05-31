# userDashboardApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.user_profile, name='user_profile'),
    path('withdraw/<int:course_id>/', views.withdraw_course, name='withdraw_course'),
]
