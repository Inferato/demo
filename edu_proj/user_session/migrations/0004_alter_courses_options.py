# Generated by Django 4.2.10 on 2024-02-27 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_session', '0003_courses_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'permissions': (('can_edit_course', 'can edit course'), ('can_add_courses', 'User can add courses'), ('can_set_permission', 'User can set permissions to other users'))},
        ),
    ]
