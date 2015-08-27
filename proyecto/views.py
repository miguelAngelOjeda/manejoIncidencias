#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from proyecto.models import Proyecto
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import ProyectoForm

# Create your views here.
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render_to_response('proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))

def nuevo_proyecto(request):
    if request.method=='POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ProyectoForm()
    return render_to_response('proyectoForm.html',{'formulario':formulario}, context_instance=RequestContext(request))