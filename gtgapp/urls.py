from django.conf.urls import patterns, include, url

from django.contrib import admin
#from equipment.views import HelloTemplate
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtgapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #whenever someone types in site.com/equipment/*anything*, they'll be routed to the urls.py
    #file in the equipment folder.
    #Special note: we don't need ot put URL at the beginning because we're doing that elsewhere.
    (r'^equipment/', include('equipment.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^hello/$', 'equipment.views.hello'),
#    url(r'^hello_template/$', 'equipment.views.hello_template'),
#	url(r'^hello_template_simple/$', 'equipment.views.hello_template_simple'),
#	url(r'^hello_class_view/$', HelloTemplate.as_view()),

)
