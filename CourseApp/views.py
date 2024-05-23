# CourseApp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseFilterForm
from django.db.models import Q

def course_list(request):
    form = CourseFilterForm(request.GET)
    courses = Course.objects.all()

    # Check if any filter fields are present in the request GET parameters
    has_filter = any(field in request.GET for field in form.fields.keys())

    if form.is_valid():
        category = form.cleaned_data.get('category')
        difficulty_level = form.cleaned_data.get('difficulty_level')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if category:
            courses = courses.filter(category=category)
        if difficulty_level:
            courses = courses.filter(difficulty_level=difficulty_level)
        if min_price is not None:
            courses = courses.filter(price__gte=min_price)
        if max_price is not None:
            courses = courses.filter(price__lte=max_price)

    return render(request, 'CourseApp/courselist.html', 
                  {'courses': courses, 'form': form, 'has_filter': has_filter})

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

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Add the logic for enrolling the user in the course here
    # e.g., creating an enrollment record in the database
    # Enrollment.objects.create(user=request.user, course=course)
    return redirect('course_list')
