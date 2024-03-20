from django.contrib import admin
from .models import UserCourses, Courses

class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name',)

admin.site.register(UserCourses, UserCoursesAdmin)
admin.site.register(Courses, CoursesAdmin)

