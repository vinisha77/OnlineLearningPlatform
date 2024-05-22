# CourseApp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.db.models import Q

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'CourseApp/courselist.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'CourseApp/coursedetails.html', {'course': course})

def search_courses(request):
    query = request.GET.get('query')
    courses = Course.objects.all()

    if query:
        courses = Course.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        courses = []
    return render(request, 'CourseApp/search_results.html', {'courses': courses, 'query': query})
