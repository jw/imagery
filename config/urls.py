# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

# FIXME: omg! remove this!
from imagery.impart import views as impart_views
from imagery.artist import views as artist_views
from imagery.images import views as images_views

urlpatterns = [
    url(r'^about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('imagery.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # imagery: images, artist and impart
    url(r'^$', images_views.artists, name='home'),
    url(r'^artist/', artist_views.artist),
    url(r'^news/', impart_views.news),
    url(r'^archive/', impart_views.archive),
    url(r'^manifest/', impart_views.manifest),
    url(r'^landprice/', impart_views.landprice),

    # TODO: handle this - should this be there?
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

    url(r'^s3direct/', include('s3direct.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
