from django.shortcuts import render_to_response
from equipment.models import *

"""def getalltypes():
    e = EquipmentType.objects.select_related()
    dict = {}
    for i in e:
        if str(i.equipment_class) in dict:
            dict[str(i.equipment_class)].append(str(i))
        else:
            dict[str(i.equipment_class)].append(str(i))
    return dict
"""

def equipmentlist(request):
    return render_to_response('equipmentlist.html',
                              {'equipmentlist': EquipmentType.objects.all()}
                            )


def equipmentclass(request, equipment_class_id=1):  # Where #1 is the default, not a hardcoded value
    return render_to_response('equipmentclass.html',
                              {'equipmentclass': EquipmentClass.objects.get(id=equipment_class_id)})


"""from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView


# Create your views here.
def hello(request):
    name= "Aaron"
    html = "<html><body>Hi %s. This seems to have worked!</html></body>" % name
    return HttpResponse(html)

#This is a non class-based view, which calls a template and sets certain arguments to stated values.
def hello_template(request):
    name = "Aaron"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

#This is a shortcut view, where you tell it the name of the template and pass it arguments. It functions the same as hello_template.
def hello_template_simple(request):
    name = "Aaron"
    return render_to_response('hello.html', {'name': name})

#This is a class-based view, which takes a template name, and ... I'm not totally sure why I'd use this.
class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        #Super is used to get a value from something outside of this method.
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Aaron'
        return context"""
