from django.views.generic.simple import direct_to_template

def index(request):
    extra_context = {
            'motd' : 'Welcome to the koi.io demo',
    }
    return direct_to_template(request, template="index.html", extra_context=extra_context)
