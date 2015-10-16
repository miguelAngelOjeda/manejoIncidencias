from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from proyecto.models import Proyecto
from forms import RolForm
from models import Rol

# Create your views here.
def grupos(request):
    usuario = request.user
    rol = Rol.objects.all()
    return render_to_response('rol.html',{'flujos':rol,'usuario':usuario}, context_instance=RequestContext(request))

def nuevo_grupo(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo flujo
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = RolForm(request.POST)
        if formulario.is_valid:
            try:
                proyecto = Proyecto.objects.get(scrum_master=usuario)

                formulario.proyecto = proyecto
                rol = formulario.save()
                rol = get_object_or_404(Rol, pk=rol.id)
                rol.proyecto = proyecto
                rol.save()
                return HttpResponseRedirect('/../flujos')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear_grupo.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
    else:
        formulario = RolForm()
    return render_to_response('crear_grupo.html', {'formulario': formulario,'usuario':usuario}, context_instance=RequestContext(request))

def lista_usuarios(request, pk_rol):
    usuario = request.user
    rol = get_object_or_404(Rol, pk=pk_rol)
    roles = rol.usuario.all()

    return render_to_response('lista_usuarios.html',{'flujos':roles,'usuario':usuario}, context_instance=RequestContext(request))