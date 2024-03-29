# Generated by Django 4.2.10 on 2024-02-23 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='usercourses',
            name='course_name',
        ),
        migrations.AddField(
            model_name='usercourses',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_session.courses'),
        ),
    ]
