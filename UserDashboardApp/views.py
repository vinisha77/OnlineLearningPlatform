# userDashboardApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from CourseApp.models import Enrollment
from .forms import UserProfileForm

@login_required
def dashboard(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'enrollments': enrollments, 'current_view': 'dashboard'})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form},)

@login_required
def withdraw_course(request, course_id):
    enrollment = get_object_or_404(Enrollment, user=request.user, course_id=course_id)
    enrollment.delete()
    return redirect('dashboard')
