from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .forms import CourseSelectionForm, LevelSelectionForm
from .models import PersonalizedLearningPath, Level
from CourseApp.models import Course  # Importing Course model from Course app
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def login_required_message(message='You must be logged in to access this page.'):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.info(request, message)
                return redirect('user_login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@login_required_message('You need to log in to create a personalized learning path.')
def select_course(request):
    if request.method == 'POST':
        selected_course_ids = request.POST.getlist('course_ids')
        selected_level = request.POST.get('level')

        print("Selected course IDs:", selected_course_ids)  # Debugging
        print("Selected level:", selected_level)  # Debugging

        if selected_course_ids and selected_level:
            # Assuming we take the first selected course for simplicity
            selected_course_id = selected_course_ids[0]
            request.session['course_id'] = selected_course_id
            request.session['level_id'] = selected_level

            # Create a new PersonalizedLearningPath instance
            course = Course.objects.get(id=selected_course_id)
            user = request.user

            # Here we assume a default level, you can adjust this based on your requirements
            level = Level.objects.get(name=selected_level)  # Assuming a default level for now
            learning_path = PersonalizedLearningPath.objects.create(user=user, course=course, level=level)
            learning_path.save()
            
            return redirect('view_learning_path', path_id=learning_path.id)
        else:
            if not selected_level:
                messages.error(request, 'Please select a level.')
            else:
                messages.error(request, 'Please select one course.')
    categories = [
        ('programming', 'Programming'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('security', 'Security'),
    ]
    courses = Course.objects.all()
    levels = Level.objects.all()
    return render(request, 'personalpath/select_course.html', {'categories': categories, 'courses': courses, 'levels': levels})

@login_required_message('You need to log in to create a personalized learning path.')
def view_learning_path(request, path_id):
    try:
        path = PersonalizedLearningPath.objects.get(id=path_id)
        course = path.course
        level = path.level
        username = request.user.username
    except PersonalizedLearningPath.DoesNotExist:
        messages.error(request, 'Learning path not found.')
        return redirect('select_course')

    return render(request, 'personalpath/view_learning_path.html', {'path': path , 'username': username, 'course': course, 'level':level})


def select_level(request):
    from .models import Level   #Import the Level model
