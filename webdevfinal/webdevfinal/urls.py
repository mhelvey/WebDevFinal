from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webdevfinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^homepage/education', 'homepage.views.education'),
    url(r'^homepage/experience', 'homepage.views.experience'),
    url(r'^homepage/about', 'homepage.views.base'),
    url(r'^homepage/adventures', 'homepage.views.adventures'),
    url(r'^homepage/', 'homepage.views.base'),


    url(r'^admin/', include(admin.site.urls)),
)
