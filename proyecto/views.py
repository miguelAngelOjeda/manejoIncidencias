#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from proyecto.models import Proyecto
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import ProyectoForm,ProyectoEditarForm
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import get_current_timezone

# Create your views here.
def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render_to_response('proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))

def nuevo_proyecto(request):
    if request.method=='POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('proyectoForm.html',{'formulario':formulario,'errors':error}, context_instance=RequestContext(request))
    else:
        formulario = ProyectoForm()
    return render_to_response('proyectoForm.html',{'formulario':formulario}, context_instance=RequestContext(request))

def consultarProyecto(request, pk_proyecto):
     """ Recibe un request y un id, luego busca en la base de datos al proyecto
    cuyos datos se quieren consultar.

	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista

	@type pk_proyecto: Integer
	@param pk_proyecto: identificador unico del proyecto

	@rtype: django.HttpResponse
	@return: visualizarProyecto.html, donde se le despliega al proyecto los datos

	@author: Miguel Ojeda
	"""
     proyecto = Proyecto.objects.get(pk=pk_proyecto)
     return render_to_response('visualizarProyecto.html', {'proyecto': proyecto}, context_instance=RequestContext(request))


def desactivar(request, pk_proyecto):
    """
    Funcion que inactiva la cuenta de un proyecto seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_proyecto: Integer
    @param pk_proyecto: id del proyecto a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza proyectos/delete.html para obtener el formulario o
            redirecciona a la vista index de proyectos si el proyecto fue desactivado.
    """

    proyecto_detail = get_object_or_404(Proyecto, pk=pk_proyecto)
    proyecto_detail.is_active = False
    proyecto_detail.save()
    mensaje ="El proyecto se desactivo con exito."

    usuario = Proyecto.objects.all()
    return render_to_response('proyectos.html', {'proyectos': usuario,'mensajes':mensaje}, context_instance=RequestContext(request))

def activar(request, pk_proyecto):
    """
    Funcion que inactiva la cuenta de un proyecto seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_proyecto: Integer
    @param pk_proyecto: id del proyecto a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza proyectos/delete.html para obtener el formulario o
            redirecciona a la vista index de proyectos si el proyecto fue desactivado.
    """

    proyecto_detail = get_object_or_404(Proyecto, pk=pk_proyecto)
    proyecto_detail.is_active = True
    proyecto_detail.save()

    mensaje ="El usuario se activo con exito."

    usuario = Proyecto.objects.all()
    return render_to_response('proyectos.html', {'proyectos': usuario,'mensajes':mensaje}, context_instance=RequestContext(request))

