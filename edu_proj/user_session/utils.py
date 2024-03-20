from django.shortcuts import redirect
from .my_form import SetUserCourseForm


def process_request_session(request): 
    if request.method == 'POST':
        form = create_form(request_data=request.POST)
        if form.is_valid():
            request.session['user_input'] = form.cleaned_data
            redirect('display_user_input')
    
def create_form(request_data=None):
    if request_data:
        return SetUserCourseForm(request_data)
    
    return SetUserCourseForm()

def user_can_edit(request, model):
    user = request.user
    if not user.is_anonymous:
        return model.can_edit(user)
    return False
