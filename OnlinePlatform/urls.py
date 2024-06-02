from django.urls import path, include
from django.contrib import admin
from django.conf import settings
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
