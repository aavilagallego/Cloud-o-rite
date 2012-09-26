from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
dajaxice_autodiscover()


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'newsmgr.views.home', name='home'),
    # url(r'^cloudorite/', include('cloudorite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', 'newsmgr.views.home', name='home'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^addnew/', 'newsmgr.views.addnew', name='addnew'),
)

urlpatterns += staticfiles_urlpatterns()

