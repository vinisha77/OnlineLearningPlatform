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
from CourseApp.models import Course

# Create your views here.

def home(request):
    return render (request , 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        user = authenticate(username=username,password=password)
 
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('course_list'))
           
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!")
           
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
   
    else:
        return render(request, 'UserApp/login.html',{})
    
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
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('user_login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'UserApp/registration.html', {'form': form})

def search_courses(request):
    pass

def category_courses(request, category):
    courses = Course.objects.filter(category=category)
    return render(request, 'category_courses.html', {'courses': courses})
