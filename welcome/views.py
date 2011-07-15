from django.views.generic.simple import direct_to_template
from django.core.cache import cache

def index(request):
    cache.set('secret', 'roses are red, violets are blue')
    extra_context = {
            'motd' : 'Welcome to the stackrocket.com demo',
            'secret' : cache.get('secret')
    }
    return direct_to_template(request, template="index.html", extra_context=extra_context)
