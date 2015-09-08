from django.conf.urls import (  # noqa
    patterns, include, url, handler404, handler500,
)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('demoapp.views',
    # Examples:
    url(r'^$', 'home'),
    # url(r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^add/(\d+)/(\d+)$', 'add'),
    url(r'^mul/(\d+)/(\d+)$', 'mul'),    
)
