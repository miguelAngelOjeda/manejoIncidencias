from django.shortcuts import render
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from usuario.models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from forms import UserCreateForm


# Create your views here.
def usuarios(request):
    usuario = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario}, context_instance=RequestContext(request))


def nuevo_usuario(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo usuario
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    if request.method == 'POST':
        formulario = UserCreateForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreateForm()
    return render_to_response('crear.html', {'formulario': formulario}, context_instance=RequestContext(request))


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
    if request.method == 'POST':
        user_detail = get_object_or_404(User, pk=pk_usuario)
        user_detail.is_active = False
        user_detail.save()

        return HttpResponseRedirect('/usuarios/')

    user_detail = get_object_or_404(User, pk=pk_usuario)

    return render(request, 'usuarios/delete.html', locals())
