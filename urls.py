from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
from django.views.generic.simple import redirect_to


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VerdeBinario.views.home', name='home'),
    # url(r'^VerdeBinario/', include('VerdeBinario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),    
    url(r'^museo/foto/(?P<id>\d+)/$', 'VerdeBinario.museo.views.VediFoto', name='vedi_foto'),
    (r'^$', redirect_to, {'url': '/admin/'}),


)


