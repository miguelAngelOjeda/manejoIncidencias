from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from proyecto.models import Proyecto
from forms import ActividadCreateForm, FlujoCreateForm
# from form import AsignarFlujoProyectoForm
from models import Flujo, Actividad, Estado

# Create your views here.
from user_story.models import UserStory


def flujos(request):
    usuario = request.user
    flujos = Flujo.objects.all()
    return render_to_response('flujos.html', {'flujos': flujos, 'usuario': usuario},
                              context_instance=RequestContext(request))


def actividades(request):
    usuario = request.user
    actividades = Actividad.objects.all()
    user_story = UserStory.objects.all()
    return render_to_response('actividades.html',
                              {'actividades': actividades, 'usuario': usuario, 'user_story': user_story},
                              context_instance=RequestContext(request))


def nueva_actividad(request):
    """
    Funcion que recibe un request y devuelve un response para crear una nueva actividad
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = ActividadCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../actividades')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_actividad.html',
                                          {'formulario': formulario, 'errors': error, 'usuario': usuario},
                                          context_instance=RequestContext(request))
    else:
        formulario = ActividadCreateForm()
    return render_to_response('crear_actividad.html', {'formulario': formulario, 'usuario': usuario},
                              context_instance=RequestContext(request))


def nuevo_flujo(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo flujo
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = FlujoCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../flujos')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_flujo.html',
                                          {'formulario': formulario, 'errors': error, 'usuario': usuario},
                                          context_instance=RequestContext(request))
    else:
        formulario = FlujoCreateForm()
    return render_to_response('crear_flujo.html', {'formulario': formulario}, context_instance=RequestContext(request))


def desactivar(request, pk_flujo):
    """
    Funcion que inactiva la cuenta de un flujo seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_flujo: Integer
    @param pk_flujo: id del flujo a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza flujos/delete.html para obtener el formulario o
            redirecciona a la vista index de flujos si el flujo fue desactivado.
    """
    usuariolB = request.user
    user_detail = get_object_or_404(Actividad, pk=pk_flujo)
    user_detail.is_active = False
    user_detail.save()
    mensaje = "El usuario se desactivo con exito."

    usuario = Actividad.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario, 'mensajes': mensaje, 'usuario': usuariolB},
                              context_instance=RequestContext(request))


def activar(request, pk_flujo):
    """
    Funcion que inactiva la cuenta de un flujo seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_flujo: Integer
    @param pk_flujo: id del flujo a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza flujos/delete.html para obtener el formulario o
            redirecciona a la vista index de flujos si el flujo fue desactivado.
    """
    usuariolB = request.user
    user_detail = get_object_or_404(Actividad, pk=pk_flujo)
    user_detail.is_active = True
    user_detail.save()

    mensaje = "El usuario se activo con exito."

    usuario = Actividad.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario, 'mensajes': mensaje, 'usuario': usuariolB},
                              context_instance=RequestContext(request))
