from django.urls import path
from .views import (
    InputPage, 
    display_user_courses_view, 
    UserCoursesView, 
    UserCoursesListView, 
    AddModelPermissionView,
    upload_file,
    file_list,
    honey_pot,
)

urlpatterns = [
    path('user-input/<int:course_id>/', InputPage.as_view(), name='user_input'),
    path('user-input/', InputPage.as_view(), name='user_input'),
    path('display-user-courses/', display_user_courses_view, name='display_user_input'),
    path('courses/', UserCoursesListView.as_view(), name='list_courses'),
    path('courses/add/', UserCoursesView.as_view(), name='add_course'),
    path('courses/<int:course_id>/edit/', UserCoursesView.as_view(), name='edit_course'),
    path('add_model_permission/', AddModelPermissionView.as_view(), name='add_model_permission'),
    path('upload/', upload_file, name='upload_file'),
    path('file_list/', file_list, name='file_list'),
    path('display-form/', honey_pot, name='display_form' )
]