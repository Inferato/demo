# Generated by Django 4.2.10 on 2024-02-27 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_session', '0004_alter_courses_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'permissions': (('can_edit_course', 'User can edit course(custom)'), ('can_add_courses', 'User can add courses(custom)'), ('can_set_permission', 'User can set permissions to other users(custom)'))},
        ),
    ]
