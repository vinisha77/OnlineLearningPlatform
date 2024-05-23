from django.shortcuts import render,redirect,get_object_or_404
from .forms import CourseForm
from .models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'CourseApp/course_list.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redirect to the course list view after saving
    else:
        form = CourseForm()
    
    return render(request, 'CourseApp/create_edit_course.html', {'form': form})



@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user != course.instructor:
        return redirect('course_detail', pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'CourseApp/course_form.html', {'form': form})
    

@login_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user == course.instructor:
        course.delete()
    return redirect('course_list')
    

