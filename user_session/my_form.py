from django import forms

class MyForm(forms.Form):
    username = forms.CharField(label="My username field")
    email = forms.EmailField(label="Your Email")
    course_name = forms.CharField(label="Course name", required=False)
