from django.shortcuts import redirect
from .my_form import MyForm


def process_request_session(request): 
    if request.method == 'POST':
        form = create_form(request_data=request.POST)
        if form.is_valid():
            request.session['user_input'] = form.cleaned_data
            redirect('display_user_input')
    
def create_form(request_data=None):
    if request_data:
        return MyForm(request_data)
    
    return MyForm()