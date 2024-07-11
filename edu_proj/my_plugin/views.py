from django.http import HttpResponse

def plugin_view(request):
    return HttpResponse("This is a plugin response! (=")