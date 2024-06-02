# CourseApp/admin.py

from django.contrib import admin
from .models import Course, Enrollment

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    readonly_fields = ('user', 'course', 'enrolled_at')

class CourseAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
    list_display = ('title', 'description', 'price', 'link',)
    list_editable = ('link',)  

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment) 
