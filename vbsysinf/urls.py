from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

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
#    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),
    url(r'^museo/foto/(?P<id>\d+)/$', 'museo.views.VediFoto', name='vedi_foto'),
    (r'^$', RedirectView.as_view(url='/admin/')),


)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


