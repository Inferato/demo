from django import template
from django.template.defaultfilters import stringfilter
from ..models import UserCourses

register = template.Library()


@register.filter(name="test_format")
def trim_message(value, strip_args="<p></p>"):
    # if value:
    #     return value.strip("<p></p>")
    # else:
    #     return ""

    if not value:
        return ""
    
    if isinstance(value, str):
        return value.strip(strip_args)
    else:
        return value
    
@register.inclusion_tag('user_courses.html')
def show_user_courses(user):
    user_courses = UserCourses.objects.filter(user=user)
    return {'user_courses': user_courses}