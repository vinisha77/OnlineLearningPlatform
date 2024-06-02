# CourseApp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Course, Enrollment
from .forms import CourseFilterForm
from django.db.models import Q

def home(request):
    categories = Course.CATEGORY_CHOICES
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context)

def course_list(request):
    form = CourseFilterForm(request.GET)
    courses = Course.objects.all()
    user_enrollments = get_user_enrollments(request.user) if request.user.is_authenticated else []

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
                  {'courses': courses, 'form': form, 'has_filter': has_filter, 'user_enrollments': user_enrollments})

def get_user_enrollments(user):
    if user.is_authenticated:
        return Enrollment.objects.filter(user=user).values_list('course_id', flat=True)
    else:
        return []

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'CourseApp/coursedetails.html', {'course': course})

def search_courses(request):
    query = request.GET.get('q')
    courses = Course.objects.all()
   
    courses = Course.objects.filter(title__icontains=query) | Course.objects.filter(author__icontains=query) | Course.objects.filter(description__icontains=query)
              
    return render(request, 'CourseApp/search_results.html', {'courses': courses, 'query': query})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user

    # Check if user is already enrolled in the course
    if Enrollment.objects.filter(user=user, course=course).exists():
        messages.info(request, 'You are already enrolled in this course.')
    else:
        # Enroll the user in the course
        Enrollment.objects.create(user=user, course=course)
        messages.success(request, 'Successfully enrolled in the course.')

    return redirect('course_detail', course_id=course_id)

def category_courses(request, category):
    courses = Course.objects.filter(category=category)
    # Get the enrollments of the current user
    user_enrollments = []
    if request.user.is_authenticated:
        user_enrollments = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)

    context = {
        'category': category,
        'courses': courses,
        'user_enrollments': user_enrollments,  # Pass the user's enrollments to the template
    }
    return render(request, 'category_courses.html', context)

def category_course_detail(request, course_id):
    # Retrieve the course object using the course_id
    course = get_object_or_404(Course, id=course_id)

    # Get the enrollments of the current user
    user_enrollments = []
    if request.user.is_authenticated:
        user_enrollments = Enrollment.objects.filter(user=request.user).values_list('course_id', flat=True)

    context = {
        'course': course,
        'user_enrollments': user_enrollments,  # Pass the user's enrollments to the template
    }

    # Render the template with the course detail
    return render(request, 'category_course_details.html', context)
