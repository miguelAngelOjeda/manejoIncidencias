from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext

from user_story.forms import UserStoryCreateForm, UserStoryFlujoForm
from user_story.models import UserStory, Flujouserstory


# Create your views here.


def lista_user_story(request):
    """
    Funcion que recibe un request y devuelve la lista de los User Story
    @param request:
    @type request: django.http.HttpRequest.
    @return: Lista de User Story
    @rtype: render_to_response.
    """
    user_story = UserStory.objects.all()
    flujo_user_story = Flujouserstory.objects.all()
    return render_to_response('userstory.html', {'user_story': user_story, 'flujo_user_story': flujo_user_story},
                              context_instance=RequestContext(request))


def nuevo_userstory(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo User Story
    @param request:
    @type request: django.http.HttpRequest.
    @return: Formulario
    @rtype: render_to_response.
    """
    if request.method == 'POST':
        formulario = UserStoryCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../userstory')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_userstory.html', {'formulario': formulario, 'errors': error},
                                          context_instance=RequestContext(request))
    else:
        formulario = UserStoryCreateForm()
    return render_to_response('crear_userstory.html', {'formulario': formulario},
                              context_instance=RequestContext(request))


def consultar_estado(request, id_user_story):
    """
    Funcion que recibe un request y una id de un User Story especifico y devuelve un response que contiene el estado
    Kanbam del User Story
    @param request:
    @type request:
    @param id_user_story:
    @type id_user_story: int
    @return: User Story
    @rtype: render_to_response
    """
    flujo_story = Flujouserstory.objects.get(id=id_user_story)
    if request.method == 'POST':
        formulario = UserStoryFlujoForm(request.POST, instance=flujo_story)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../userstory')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario, 'error': error},
                                          context_instance=RequestContext(request))
    else:
        formulario = UserStoryFlujoForm(instance=flujo_story)
        return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario},
                                  context_instance=RequestContext(request))


def estados(request):
    """
    Funcion que recibe un request y devuelve un response
    @param request:
    @type request:
    @return: Lista de estados Kanbam de User Story
    @rtype: render_to_response
    """
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
    return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario},
                              context_instance=RequestContext(request))
