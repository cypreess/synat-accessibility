from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'', include('synat_help.help_example.urls')),

#    url(r'^aaa/$', include('synat_help.help_example.urls')),
#

)
