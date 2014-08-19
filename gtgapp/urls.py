import django.conf.urls
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = django.conf.urls.patterns('',
    # Examples:
    # url(r'^$', 'gtgapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #whenever someone types in site.com/equipment/*anything*, they'll be routed to the urls.py
    #file in the equipment folder.
    #Special note: we don't need ot put URL at the beginning because we're doing that elsewhere.
    (r'^equipment/', django.conf.urls.include('equipment.urls')),
    django.conf.urls.url(r'^admin/', django.conf.urls.include(admin.site.urls)),
    (r'^$', RedirectView.as_view(url='/equipment/list/')), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    url(r'^hello/$', 'equipment.views.hello'),
#    url(r'^hello_template/$', 'equipment.views.hello_template'),
#	url(r'^hello_template_simple/$', 'equipment.views.hello_template_simple'),
#	url(r'^hello_class_view/$', HelloTemplate.as_view()),
