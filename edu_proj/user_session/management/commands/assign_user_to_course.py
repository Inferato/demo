from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from user_session.models import Courses, UserCourses
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Assign user(-s) to a specific course"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--username', type=str, help='Leave blank to assgin all users')
        parser.add_argument('--course_id', type=int, help='Desired Course ID')
        parser.add_argument('--course_name', type=str, help='Provide course name for new course')

    def handle(self, *args: Any, **options: Any) -> str | None:
        username = options['username']
        course_id = options['course_id']
        course_name = options['course_name']
        course = None

        if any([course_name, course_id]):
            if course_id:
                self.stdout.write(f'Trying to get course with ID = {course_id}')
                course = Courses.objects.filter(id=course_id).first()
            
            if not course and course_name:
                course, created = Courses.objects.get_or_create(course_name=course_name)
                if created:
                    self.stdout.write(f'Created course with name "{course_name}"')
            
        if course:
            users = []
            if username:
                user = User.objects.filter(username=username).first()
                users.append(user)
            else:
                users = User.objects.all()

            for user in users:
                if user:
                    self.stdout.write(f'Processed User "{user.username}"!')
                    user_course, uc_created = UserCourses.objects.get_or_create(user=user, course=course)
                    assign_message = f'User successfuly assigned to course "{course.course_name}"' if uc_created else f'User {user.username} is already assigned to course "{course.course_name}"'
                    self.stdout.write(assign_message)

