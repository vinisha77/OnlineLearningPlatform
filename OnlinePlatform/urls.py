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
from CourseApp import views as course_views  # Import the home view from CourseApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_views.home, name='home'),  # Use CourseApp's home view
    path('', include('UserApp.urls')),  # Include UserApp URLs
    path('userdashboard/', include('UserDashboardApp.urls')),  # Include UserDashboardApp URLs
    path('courses/', include('CourseApp.urls')),  # Include CourseApp URLs
    path('instructor/', include('InstructorApp.urls')), #Include InstructorApp URLs
    path('personalpath/', include('personalpath.urls')),  # Include personalpath URLs
]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
