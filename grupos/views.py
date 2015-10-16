from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from proyecto.models import Proyecto
from forms import GrupoForm
from models import Grupo
# Create your views here.


def grupos_listar(request):
    usuario = request.user
    gupos = Grupo.objects.all()
    return render_to_response('grupos.html',{'flujos':gupos,'usuario':usuario}, context_instance=RequestContext(request))

def grupo_nuevo(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo grupo
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = GrupoForm(request.POST)
        if formulario.is_valid:
            try:
                rol = formulario.save()

                return HttpResponseRedirect('/../grupo')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('grupo_crear.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
    else:
        formulario = GrupoForm()
    return render_to_response('grupo_crear.html', {'formulario': formulario,'usuario':usuario}, context_instance=RequestContext(request))

def lista_usuarios(request, pk_grupo):
    usuario = request.user
    rol = get_object_or_404(Grupo, pk=pk_grupo)
    roles = rol.usuarios.all()

    return render_to_response('lista_usuarios.html',{'flujos':roles,'usuario':usuario}, context_instance=RequestContext(request))