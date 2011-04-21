from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #(r'', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'})
    (r'', 'koi.welcome.views.index'),
)
