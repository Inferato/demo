from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Courses

User = get_user_model()

class SetUserCourseForm(forms.Form):
    username = forms.CharField(label="My username field")
    email = forms.EmailField(label="Your Email")

    def __init__(self, *args, **kwargs):
        super(SetUserCourseForm, self).__init__(*args, **kwargs)
        self.fields['course_name'] = forms.ChoiceField(
            label="Course name",
            choices=self.get_course_choices(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=False
        )

    def get_course_choices(self):
        course_choices = [('', '--------')]  # Initial empty choice
        user_courses = Courses.objects.all()  # Fetch courses from the database
        for course in user_courses:
            course_choices.append((course.course_name, course.course_name))
        return course_choices


class UserCoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name']


class AddPermissionForm(forms.Form):
    codenames = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Permissions'
    )

    # class Meta:
    #     model = Permission
    #     fields = ['codename', 'content_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        content_type = ContentType.objects.filter(model='courses').first()

        # self.fields['content_type'].queryset = content_type
        self.fields['codenames'].queryset = Permission.objects.filter(content_type=content_type)
        

class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True), label='Select User')

