from django.db.transaction import commit
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.template import RequestContext

from user_story.forms import UserStoryCreateForm, UserStoryFlujoForm
from user_story.models import UserStory, Flujouserstory


# Create your views here.


def lista_user_story(request):
    user_story = UserStory.objects.all()
    flujo_user_story = Flujouserstory.objects.all()
    return render_to_response('userstory.html', {'user_story': user_story, 'flujo_user_story': flujo_user_story},
                              context_instance=RequestContext(request))


def nuevo_userstory(request):
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
    flujo_story = Flujouserstory.objects.get(id=id_user_story)
    if request.method == 'POST':
        formulario = UserStoryFlujoForm(request.POST, instance=flujo_story)
        if formulario.is_valid:
            try:
                # flujo_story = formulario.save(commit=False)
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
    if request.method == 'POST':
        formulario = UserStoryFlujoForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../userstory')
            except:
                error = 'Error al procesar entidad'
                return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario}, {'errors': error},
                                          context_instance=RequestContext(request))
    else:
        formulario = UserStoryFlujoForm()
    return render_to_response('nuevo_userstory_kanbam.html', {'formulario': formulario},
                              context_instance=RequestContext(request))
