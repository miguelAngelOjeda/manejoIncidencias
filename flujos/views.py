from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from proyecto.models import Proyecto
from forms import ActividadCreateForm, AsignarFlujoProyectoForm, FlujoCreateForm
from models import Flujo, Actividad,Estado

# Create your views here.

def flujos(request):
    flujos = Flujo.objects.all()
    return render_to_response('flujos.html',{'flujos':flujos}, context_instance=RequestContext(request))


def actividades(request):
    actividades = Actividad.objects.all()
    return render_to_response('actividades.html',{'actividades':actividades}, context_instance=RequestContext(request))


def nueva_actividad(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo usuario
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    if request.method == 'POST':
        formulario = ActividadCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_actividad.html',{'formulario':formulario,'errors':error}, context_instance=RequestContext(request))
    else:
        formulario = ActividadCreateForm()
    return render_to_response('crear_actividad.html', {'formulario': formulario}, context_instance=RequestContext(request))


def nuevo_flujo(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo usuario
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    if request.method == 'POST':
        formulario = FlujoCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_flujo.html',{'formulario':formulario,'errors':error}, context_instance=RequestContext(request))
    else:
        formulario = FlujoCreateForm()
    return render_to_response('crear_flujo.html', {'formulario': formulario}, context_instance=RequestContext(request))
def desactivar(request, pk_usuario):
    """
    Funcion que inactiva la cuenta de un usuario seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_usuario: string
    @param pk_usuario: id del usuario a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza usuarios/delete.html para obtener el formulario o
            redirecciona a la vista index de usuarios si el usuario fue desactivado.
    """

    user_detail = get_object_or_404(Actividad, pk=pk_usuario)
    user_detail.is_active = False
    user_detail.save()
    mensaje ="El usuario se desactivo con exito."

    usuario = Actividad.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'mensajes':mensaje}, context_instance=RequestContext(request))

def activar(request, pk_usuario):
    """
    Funcion que inactiva la cuenta de un usuario seleccionado.

    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la peticion actual

    @type pk_usuario: string
    @param pk_usuario: id del usuario a ser inactivado

    @rtype: django.http.HttpResponseRedirect
    @return: Renderiza usuarios/delete.html para obtener el formulario o
            redirecciona a la vista index de usuarios si el usuario fue desactivado.
    """

    user_detail = get_object_or_404(Actividad, pk=pk_usuario)
    user_detail.is_active = True
    user_detail.save()

    mensaje ="El usuario se activo con exito."

    usuario = Actividad.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'mensajes':mensaje}, context_instance=RequestContext(request))

