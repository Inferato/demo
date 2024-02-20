from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .my_form import MyForm
from .utils import create_form
from .models import UserCourses
from user_session import GLOB_VAR  #Case of usage variables from __init__.py


# def input_page_view(request):
#     process_request_session(request=request)
#     return render(request, 'input_page.html', {'form': create_form()})


# def display_input_view(request):
#     user_input = request.session.get('user_input', {})
#     return render(request, 'display_page.html', {'user_input': user_input})

class InputPage(View):
    template_name='input_page.html'

    def get(self, request, course_id=None):
        if course_id:
            # 1 course by ID
            return redirect('display_user_input')
        else:
            return render(request, self.template_name, {'form': create_form()})
    
    def post(self, request):
        form = create_form(request_data=request.POST)
        if form.is_valid():
            # request.session['user_input'] = form.cleaned_data
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            course_name = form.cleaned_data.get('course_name')
            user = User.objects.filter(email=email, username=username).first()
            errors = {}
            if not user:
                errors['user'] = "User doesnt exist"
            
            if not course_name:
                errors['course_name'] = "Please enter the course name"

            if not errors:
                user_course, created = UserCourses.objects.get_or_create(user=user)
                user_course.course_name=course_name
                user_course.save()

            # if not errors:
            #     user_course, created = UserCourses.objects.get_or_create(user=user)
            #     if not created:
            #         user_course.course_name=course_name
            #         user_course.save()

            return render(request, self.template_name, {'errors': errors, 'form': create_form()})

def display_user_courses_view(request):
    user_courses = UserCourses.objects.all().order_by('user')

    return render(request, 'display_page.html', {'user_courses': user_courses})
