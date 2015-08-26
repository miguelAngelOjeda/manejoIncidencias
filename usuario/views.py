from django.core.exceptions import ValidationError
from django.shortcuts import render
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from usuario.models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from forms import UserCreateForm,UsuarioEditarForm


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
            try:
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear.html',{'formulario':formulario,'errors':error}, context_instance=RequestContext(request))
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

    user_detail = get_object_or_404(User, pk=pk_usuario)
    user_detail.is_active = False
    user_detail.save()
    mensaje ="El usuario se desactivo con exito."

    usuario = Usuario.objects.all()
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

    user_detail = get_object_or_404(User, pk=pk_usuario)
    user_detail.is_active = True
    user_detail.save()

    mensaje ="El usuario se activo con exito."

    usuario = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'mensajes':mensaje}, context_instance=RequestContext(request))

def consultarUsuario(request, pk_usuario):
     """ Recibe un request y un id, luego busca en la base de datos al usuario
    cuyos datos se quieren consultar.

	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista

	@type id_usuario: Integer
	@param id_usuario: identificador unico del usuario

	@rtype: django.HttpResponse
	@return: consultar_usuario.html, donde se le despliega al usuario los datos

	@author: Miguel Ojeda
	"""
     usuario = Usuario.objects.get(pk=pk_usuario)
     return render_to_response('visualizar.html', {'usuario': usuario}, context_instance=RequestContext(request))


def usuarioEditar(request,pk_usuario):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo usuario
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = Usuario.objects.get(id=pk_usuario)
    if request.method == 'POST':
        formulario = UsuarioEditarForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.clean()
                username = formulario.cleaned_data['Nombre_de_Usuario']
                password = formulario.cleaned_data['Contrasenha']
                nuevo_password = formulario.cleaned_data['Nueva_contrasenha']
                email = formulario.cleaned_data['Email']
                first_name = formulario.cleaned_data['Nombre']
                last_name = formulario.cleaned_data['Apellido']
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear.html',{'formulario':formulario,'errors':error}, context_instance=RequestContext(request))
    else:
        formulario = UserCreateForm()
    return render_to_response('crear.html', {'formulario': formulario}, context_instance=RequestContext(request))