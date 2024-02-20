from django.contrib import admin
from .models import UserCourses

class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_name')


admin.site.register(UserCourses, UserCoursesAdmin)

