from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .my_form import UserCoursesForm, UserSelectionForm, AddPermissionForm
from .utils import create_form
from .models import UserCourses, Courses
from .mixins import (
    LoggingMixin, 
    LoginRequiredMixin as LoginMixin, 
    UserCoursesPermissionMixin, 
    SuperuserRequiredMixin,
    CacheMixin
)
# import logging

# logger = logging.getLogger(__name__)

User = get_user_model()


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
            some_data = "<br>Some text</br>"
            return render(request, self.template_name, {'form': create_form(), 'context_data': some_data})
    
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


class UserCoursesView(PermissionRequiredMixin, View):
    permission_required = ('user_session.can_edit_course')
    template_name = 'user_courses_form.html'
    
    def get(self, request, course_id=None):
        if course_id:
            course = Courses.objects.get(pk=course_id)
            form = UserCoursesForm(instance=course)
        else:
            form = UserCoursesForm()

        return render(request, self.template_name, {'form': form})
    
    def post(self, request, course_id=None):
        if course_id:
            course = Courses.objects.get(pk=course_id)
            form = UserCoursesForm(request.POST, instance=course)
        else:
            form = UserCoursesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_courses')

        return render(request, self.template_name, {'form': form})


class UserCoursesListView(LoggingMixin, View):
    template_name = 'user_courses_list.html'

    def get(self, request):
        courses = Courses.objects.all()
        return render(request, self.template_name, {'courses': courses, 'sum':sum})
    

class AddModelPermissionView(UserCoursesPermissionMixin, FormView):
    
    template_name = 'add_model_permission.html'
    form_class = AddPermissionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = Courses
        context['user_form'] = UserSelectionForm()
        return context

    def form_valid(self, form):
        selected_permissions = form.cleaned_data['codenames']
        user_form = UserSelectionForm(self.request.POST)
        if user_form.is_valid():
            selected_user = user_form.cleaned_data['user']
            # for permission in selected_permissions:
            #     selected_user.user_permissions.add(permission)
            selected_user.user_permissions.add(*selected_permissions)
        
        return redirect('list_courses')
    


    def add_two_num(a, b):
        return a+b
    
    add_two_num(2, 5)
