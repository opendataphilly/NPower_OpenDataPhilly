from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('opendata.views',
    # Examples:
    (r'^$', 'home'),
    (r'^opendata/$', 'results'),
    
    (r'^opendata/tag/(?P<tag_id>.*)/$', 'tag_results'),
    (r'^opendata/search/$', 'search_results'),
    (r'^opendata/resource/(?P<resource_id>.*)/$', 'resource_details'),
    
    (r'^tags/$', 'get_tag_list'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^_admin_/', include(admin.site.urls)),
    #(r'^accounts/', include('registration.backends.default.urls')),

    (r'^/static/admin_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.ADMIN_MEDIA_ROOT}), 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DATA}),
)
