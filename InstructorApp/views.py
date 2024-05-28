from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from CourseApp.models import Course


# Create your views here.
@login_required
def instructor_dashboard(request):
    courses = Course.objects.filter(author=request.user.username)
    return render(request, 'InstructorApp/instructor_dashboard.html', {'courses': courses})


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user.username
            course.save()
            return redirect('instructor_dashboard')
    else:
        form = CourseForm()
    return render(request, 'InstructorApp/course_form.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, author=request.user.username)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('instructor_dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'InstructorApp/course_form.html', {'form': form})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, author=request.user.username)
    if request.method == 'POST':
        course.delete()
        return redirect('instructor_dashboard')
    return render(request, 'InstructorApp/course_confirm_delete.html', {'course': course})