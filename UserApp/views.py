import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
<<<<<<< HEAD
from CourseApp.models import Course

=======
import logging
from .models import Profile  # Import the Profile model
from CourseApp.models import Course
>>>>>>> 52233234b1493bc821dd9988894d07476e17d8eb
# Create your views here.

def home(request):
    return render (request , 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        logger = logging.getLogger(__name__)
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                
                # Print the user object and role for debugging purposes
                logger.info(f"Current User: {user.username}, Role: {user.profile.role}")
                
                # Check the user's role and redirect accordingly
                if user.profile.role == 'instructor':
                    return redirect('instructor_dashboard')
                else:
                    return redirect('course_list')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
        else:
            logger.warning(f"Login failed for Username: {username}")
            messages.error(request, "Invalid login details supplied!")
            return render(request, 'UserApp/login.html', {})
    else:
        return render(request, 'UserApp/login.html', {})

    
    #context = {}  # Define an empty context or use getcontext() if defined elsewhere
    #return render(request, 'UserApp/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            
            # Update the profile with the role and is_instructor information
            profile = user.profile
            profile.role = role
            profile.is_instructor = (role == 'instructor')
            profile.save()
            
            login(request, user)
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'UserApp/registration.html', {'form': form})

def search_courses(request):
    pass

@login_required
def course_detail(request):
    pass

def course_list(request):
    pass



@login_required
def instructor_dashboard(request):
    if not request.user.profile.role == 'instructor':
        return redirect('home')
    # Add any other context you want to pass to the template
    return render(request, 'InstructorApp/instructor_dashboard.html')


def category_courses(request, category):
    courses = Course.objects.filter(category=category)
    return render(request, 'category_courses.html', {'courses': courses})
