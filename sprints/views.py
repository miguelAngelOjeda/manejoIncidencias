from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import SprintModelForm
from usuario.models import Usuario
from user_story.models import UserStory
from models import Sprint


# Create your views here.
def sprints(request):
    usuario = request.user
    sprint = Sprint.objects.all()
    return render_to_response('sprints.html', {'sprints': sprint, 'usuario': usuario},
                              context_instance=RequestContext(request))


def nuevo_sprint(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo flujo
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = SprintModelForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/../sprints')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_sprint.html', {'formulario': formulario, 'errors': error,
                                                                     'usuario': usuario},
                                          context_instance=RequestContext(request))
    else:
        formulario = SprintModelForm()
    return render_to_response('crear_sprint.html', {'formulario': formulario, 'usuario': usuario},
                              context_instance=RequestContext(request))


def asignarUserStory(request, pk_sprints):
    usuario = request.user
    sprints = get_object_or_404(Sprint, pk=pk_sprints)
    userstorys = UserStory.objects.all()
    usuarios = Usuario.objects.all()
    return render_to_response('asignar_userStory.html',{'userstorys':userstorys,'sprints':pk_sprints,'usuario':usuario,'usuarios':usuarios}, context_instance=RequestContext(request))

def visualizarUserStory(request, pk_sprints):
    usuario = request.user
    sprints = get_object_or_404(Sprint, pk=pk_sprints)
    userstorys = UserStory.objects.all()
    usuarios = Usuario.objects.all()
    return render_to_response('visualizarSprint.html',{'userstorys':userstorys,'sprints':sprints,'usuario':usuario,'usuarios':usuarios}, context_instance=RequestContext(request))


