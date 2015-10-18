#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from proyecto.models import Proyecto
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import ProyectoForm,ProyectoEditarForm
from django.contrib.auth.models import User
from rol.forms import Rol
import datetime
from django.utils.timezone import get_current_timezone

# Create your views here.
def proyectos(request):
    usuario = request.user
    if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
    proyectos = Proyecto.objects.all()
    return render_to_response('proyectos.html',{'proyectos':proyectos ,'usuario':usuario}, context_instance=RequestContext(request))

def nuevo_proyecto(request):
    usuario = request.user
    if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
    if request.method=='POST':
        formulario = ProyectoForm(request.POST)
        if formulario.is_valid:
            try:
                proGurdado = formulario.save()
                proyecto = proGurdado.id
                print proyecto
                usuario = proGurdado.scrum_master
                print usuario
                rol = Rol()
                rol.usuario = usuario
                rol.proyecto = proGurdado
                rol.rol = "Scrum Master"
                rol.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('proyectoForm.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
    else:
        formulario = ProyectoForm()
    return render_to_response('proyectoForm.html',{'formulario':formulario,'usuario':usuario}, context_instance=RequestContext(request))

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
     usuario = request.user
     if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
     proyecto = Proyecto.objects.get(pk=pk_proyecto)
     return render_to_response('visualizarProyecto.html', {'proyecto': proyecto,'usuario':usuario}, context_instance=RequestContext(request))


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
    usuario = request.user
    if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
    proyecto_detail = get_object_or_404(Proyecto, pk=pk_proyecto)
    proyecto_detail.is_active = False
    proyecto_detail.save()
    mensaje ="El proyecto se desactivo con exito."

    usuario = Proyecto.objects.all()
    return render_to_response('proyectos.html', {'proyectos': usuario,'mensajes':mensaje,'usuario':usuario}, context_instance=RequestContext(request))

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
    usuario = request.user
    if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
    proyecto_detail = get_object_or_404(Proyecto, pk=pk_proyecto)
    proyecto_detail.is_active = True
    proyecto_detail.save()

    mensaje ="El usuario se activo con exito."

    usuario = Proyecto.objects.all()
    return render_to_response('proyectos.html', {'proyectos': usuario,'mensajes':mensaje,'usuario':usuario}, context_instance=RequestContext(request))

def proyectoEditar(request,pk_proyecto):
    """
    Clase que despliega el formulario para la modficacion del proyecto.

    @type pk_proyecto: Integer
	@param pk_proyecto: identificador unico del proyecto

    @ivar form_class: Formulario que se utiliza para la modficacion de proyecto
    @type form_class: django.forms

    """
    usuario = request.user
    if not usuario.is_superuser:
        return HttpResponseRedirect('/gestion')
    proyecto = Proyecto.objects.get(id=pk_proyecto)
    if request.method == 'POST':
        formulario = ProyectoEditarForm(request.POST)
        if formulario.is_valid:
            try:
                nombre_corto = request.POST['nombre_corto']
                nombre_largo = request.POST['nombre_largo']
                fecha_fin = request.POST['fecha_fin']
                fecha_inicio = request.POST['fecha_inicio']
                usuario = request.POST['scrum_master']
                if fecha_fin:
                     if fecha_fin <= fecha_inicio:
                         error = ("La fecha de finalizacion del proyecto debe ser posterior a la de fecha de inicio.")
                         return render_to_response('editarUsuario.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
                     else:
                        proyecto.fecha_fin = fecha_fin
                else:
                    fecha_fin = proyecto.fecha_fin

                fechaFin = []
                fechaFin = fecha_fin.split('/')
                fecha_fin = fechaFin[2]+'-'+fechaFin[1]+'-'+fechaFin[0]

                proyecto.nombre_corto = nombre_corto
                proyecto.nombre_largo = nombre_largo
                proyecto.fecha_fin = fecha_fin
                user = get_object_or_404(User, pk=usuario)
                proyecto.scrum_master = user
                proyecto.save()
                exito = 'El proyecto se modifico con exito'
                return render_to_response('editarProyecto.html',{'formulario':formulario,'exito':exito,'usuario':usuario}, context_instance=RequestContext(request))

            except:
                error = 'Error al procesar la entidad'
                return render_to_response('editarProyecto.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))

    else:
        data = {'nombre_corto': proyecto.nombre_corto, 'nombre_largo': proyecto.nombre_largo,'fecha_inicio': proyecto.fecha_inicio, 'fecha_fin': proyecto.fecha_fin,
                    'scrum_master': proyecto.scrum_master}
        formulario = ProyectoEditarForm(data)
    return render_to_response('editarProyecto.html', {'formulario': formulario,'usuario':usuario}, context_instance=RequestContext(request))