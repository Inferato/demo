from django.urls import path
from .views import plugin_view


urlpatterns = [
    path('plugin-response', plugin_view, name="plugin_view"),
]