from django.urls import path
from .views import InputPage, display_user_courses_view

urlpatterns = [
    path('user-input/<int:course_id>/', InputPage.as_view(), name='user_input'),
    path('user-input/', InputPage.as_view(), name='user_input'),
    path('display-user-courses/', display_user_courses_view, name='display_user_input')
]