from django.db import models
from django.contrib.auth.models import User


class UserCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)

