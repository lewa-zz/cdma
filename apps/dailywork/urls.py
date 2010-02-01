from django.conf.urls.defaults import *
from django.contrib import databrowse


urlpatterns = patterns('cdma.apps.views',
    (r'^databrowse/(.*)', databrowse.site.root),
)