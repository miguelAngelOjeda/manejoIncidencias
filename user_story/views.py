from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext
from proyecto.models import Proyecto
from user_story.forms import UserStoryCreateForm, UserStoryFlujoForm,AsignarForm
from user_story.models import UserStory, Flujouserstory
from usuario.models import Usuario
from sprints.models import Sprint
from flujos.models import Flujo
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


def lista_user_story(request):
    """
    Funcion que recibe un request y devuelve la lista de los User Story
    @param request:
    @type request: django.http.HttpRequest.
    @return: Lista de User Story
    @rtype: render_to_response.
    """
    usuario = request.user
    user_story = UserStory.objects.all()
    flujo_user_story = Flujouserstory.objects.all()
    return render_to_response('userstory.html',
                              {'user_story': user_story, 'flujo_user_story': flujo_user_story, 'usuario': usuario},
                              context_instance=RequestContext(request))


def nuevo_userstory(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo User Story
    @param request:
    @type request: django.http.HttpRequest.
    @return: Formulario
    @rtype: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = UserStoryCreateForm(request.POST)
        if formulario.is_valid:
            try:
                proyecto = Proyecto.objects.get(scrum_master=usuario)
                userStory  = UserStory();
                userStory.nombre = request.POST['nombre']
                userStory.descripcion = request.POST['descripcion']
                fecha_creacion = request.POST['fecha_creacion']
                fechaFin = fecha_creacion.split('/')
                userStory.fecha_creacion = fechaFin[2] + '-' + fechaFin[1] + '-' + fechaFin[0]
                userStory.valor_de_negocio = request.POST['valor_de_negocio']
                userStory.valor_tecnico = request.POST['valor_tecnico']
                userStory.duracion_horas = request.POST['duracion_horas']
                userStory.duracion_horas_en_sprint = request.POST['duracion_horas_en_sprint']
                userStory.prioridad = request.POST['prioridad']
                userStory.tipo = request.POST['tipo']
                userStory.proyecto = proyecto
                userStory.estado_scrum = 'Nuevo'
                userStory.save()
                return HttpResponseRedirect('/../userstory')
            except Exception as e:
                print e
                error = e
                return render_to_response('crear_userstory.html',
                                          {'formulario': formulario, 'errors': error, 'usuario': usuario},
                                          context_instance=RequestContext(request))
    else:
        formulario = UserStoryCreateForm()
    return render_to_response('crear_userstory.html', {'formulario': formulario, 'usuario': usuario},
                              context_instance=RequestContext(request))


def consultar_estado(request, id_user_story):
    """
    Funcion que recibe un request y una id de un User Story especifico y devuelve un response que contiene el estado
    Kanbam del User Story
    @param request:
    @type request:
    @param id_user_story:
    @type id_user_story: int
    @return: User Story especificado
    @rtype: render_to_response
    """
    usuario = request.user
    flujo_story = Flujouserstory.objects.get(id=id_user_story)
    if request.method == 'POST':
        formulario = UserStoryFlujoForm(request.POST, instance=flujo_story)
        if formulario.is_valid:
            try:

                formulario.save()
                return HttpResponseRedirect('/../userstory')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('nuevo_userstory_kanbam.html',
                                          {'formulario': formulario, 'error': error, 'usuario': usuario},
                                          context_instance=RequestContext(request))
    else:
        formulario = UserStoryFlujoForm(instance=flujo_story)
        return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario, 'usuario': usuario},
                                  context_instance=RequestContext(request))


def estados(request):
    """
    Funcion que recibe un request y devuelve un response que contiene todos los estados Kanbam
    @param request:
    @type request:
    @return: Lista de estados Kanbam de User Story
    @rtype: render_to_response
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = UserStoryFlujoForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../userstory')
            except:
                error = 'Error al procesar entidad'
                return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario}, {'errors': error},
                                          scontext_instance=RequestContext(request))
    else:
        formulario = UserStoryFlujoForm()
    return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario, 'usuario': usuario},
                              context_instance=RequestContext(request))

def asignarSprint(request,pk_userStory):
    story = UserStory.objects.get(id=pk_userStory)
    usuario = request.user
    if request.method == 'POST':
        formulario = AsignarForm(request.POST)
        if formulario.is_valid:
            try:
                story = UserStory.objects.get(id=pk_userStory)
                autor = request.POST['autor']
                sprint = request.POST['sprint']
                flujo = request.POST['flujo']
                story.autor = Usuario(autor)
                story.sprint = Sprint(sprint)
                story.flujo = Flujo(flujo)
                story.save()
                return HttpResponseRedirect('/../sprints')
            except Exception as e:
                print e
                error = 'Error al procesar la entidad'
                return render_to_response('asignar_sprint.html',{'formulario':formulario,'story':story,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
    else:
        formulario = AsignarForm()
    return render_to_response('asignar_sprint.html', {'formulario': formulario,'usuario':usuario,'story':story}, context_instance=RequestContext(request))
