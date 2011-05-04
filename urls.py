from django.conf.urls.defaults import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.conf import settings
from registration.views import register

from opendata.feeds import ResourcesFeed, TagFeed, IdeasFeed
from opendata.models import Resource, Idea

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    'resources': GenericSitemap({'queryset': Resource.objects.all(), 'date_field': 'created'}, priority=0.5),
    'ideas': GenericSitemap({'queryset': Idea.objects.all(), 'date_field': 'created_by_date'}, priority=0.5),
}

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'opendata.views.home'),
    (r'^opendata/$', 'opendata.views.results'),
    
    (r'^opendata/tag/(?P<tag_id>\d+)/$', 'opendata.views.tag_results'),
    (r'^opendata/search/$', 'opendata.views.search_results'),
    (r'^opendata/resource/(?P<resource_id>\d+)/$', 'opendata.views.resource_details'),
    (r'^opendata/resource/(?P<resource_id>\d+)/(?P<slug>[-\w]+)/$', 'opendata.views.resource_details'),
    (r'^ideas/$', 'opendata.views.idea_results'),
    (r'^idea/(?P<idea_id>\d+)/$', 'opendata.views.idea_results'),
    (r'^idea/(?P<idea_id>\d+)/(?P<slug>[-\w]+)/$', 'opendata.views.idea_results'),
    (r'^opendata/submit/$', 'opendata.views.suggest_content'),
    (r'^thanks/$', 'opendata.views.thanks'),   
    
    (r'^tags/$', 'opendata.views.get_tag_list'),
    
    (r'^comments/', include('django.contrib.comments.urls')), 
    url(r'^accounts/register/$',register,
           { 'backend': 'registration_backend.ODPBackend' },
       name='registration_register'),
    (r'^accounts/password_reset', 'django.contrib.auth.views.password_reset'),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^opendata/nominate/', include('suggestions.urls')),
     
    (r'^feeds/resources/$', ResourcesFeed()),
    (r'^feeds/ideas/$', IdeasFeed()),
    (r'^feeds/tag/(?P<tag_id>\d+)/$', TagFeed()),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Uncomment the next line to enable the admin:
    url(r'^_admin_/', include(admin.site.urls)),

    (r'^/static/admin_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.ADMIN_MEDIA_ROOT}), 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DATA}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
