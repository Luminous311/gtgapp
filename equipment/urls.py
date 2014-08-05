from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'equipment.views.equipmentlist'),
    ##the url called get takes a parameter (inside the brackets, called <equipment_id>, followed by
    ##a regex representing type, which is a digit of an arbitrary length that represents a DB ID
    url(r'^getclass/(?P<equipment_class_id>\d+)/$', 'equipment.views.equipmentclass'),
)