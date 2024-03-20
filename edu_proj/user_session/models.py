from django.db import models
from django.contrib.auth import get_user_model


class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        permissions = (
            ("can_edit_course", "User can edit course(custom)"),
            ("can_add_courses", "User can add courses(custom)"),
            ("can_set_permission", "User can set permissions to other users(custom)")
        )

    @classmethod
    def can_edit(cls, user):
        return user == cls.author


class UserCourses(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
