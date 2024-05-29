"""
URL configuration for OnlinePlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from UserApp import views as user_views
from django.conf.urls.static import static
from django.urls import path
from personalpath.views import select_course, select_level, view_learning_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
   
    path('user_register/', user_views.user_register, name='user_register'),
    path('user_login/', user_views.user_login, name='user_login'),
    path('logout/', user_views.user_logout, name='user_logout'),
    path('courses/', include('CourseApp.urls')),  # Include CourseApp URLs
    #path('course_register/', user_views.user_register, name='user_register'),
    path('instructor/', include('InstructorApp.urls')), #Include InstructorApp URLs
    path('select-course/', select_course, name='select_course'),
    path('select-level/', select_level, name='select_level'),
    path('learning-path/<int:path_id>/',view_learning_path, name='view_learning_path'),

]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
