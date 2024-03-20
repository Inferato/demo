from django import forms
from django.contrib import admin
from .models import MyCustomUser


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = MyCustomUser
        fields = ('phone_number', 'username', 'email')

class MyCustomUserAdmin(admin.ModelAdmin):
    # form = CustomUserAdminForm
    pass

admin.site.register(MyCustomUser, MyCustomUserAdmin)
