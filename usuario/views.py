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
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.
def usuarios(request):
    usuarioLo = request.user
    usuario = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'usuario':usuarioLo}, context_instance=RequestContext(request))


def nuevo_usuario(request):
    """
    Funcion que recibe un request y devuelve un response para crear un nuevo usuario
    @param request: django.http.HttpRequest.
    @return: render_to_response.
    """
    usuario = request.user
    if request.method == 'POST':
        formulario = UserCreateForm(request.POST)
        if formulario.is_valid:
            try:
                formulario.save()
                return HttpResponseRedirect('/')
            except:
                error = 'Error al procesar la entidad'
                return render_to_response('crear.html',{'formulario':formulario,'errors':error,'usuario':usuario}, context_instance=RequestContext(request))
    else:
        formulario = UserCreateForm()
    return render_to_response('crear.html', {'formulario': formulario,'usuario':usuario}, context_instance=RequestContext(request))


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
    usuario = request.user
    user_detail = get_object_or_404(User, pk=pk_usuario)
    user_detail.is_active = False
    user_detail.save()
    mensaje ="El usuario se desactivo con exito."

    usuario = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'mensajes':mensaje,'usuario':usuario}, context_instance=RequestContext(request))

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
    usuarioLo = request.user
    user_detail = get_object_or_404(User, pk=pk_usuario)
    user_detail.is_active = True
    user_detail.save()

    mensaje ="El usuario se activo con exito."

    usuario = Usuario.objects.all()
    return render_to_response('usuarios.html', {'usuarios': usuario,'mensajes':mensaje,'usuario':usuarioLo}, context_instance=RequestContext(request))

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
    Clase que despliega el formulario para la modficacion del usuario.

    @type id_usuario: Integer
	@param id_usuario: identificador unico del usuario

    @ivar form_class: Formulario que se utiliza para la modficacion de usuario
    @type form_class: django.forms

    """
    usuarioLo = request.user
    usuario = Usuario.objects.get(id=pk_usuario)
    if request.method == 'POST':
        formulario = UsuarioEditarForm(request.POST)
        if formulario.is_valid:
            try:
                user = get_object_or_404(User, pk=usuario.user.id)
                print request.POST['last_name']
                password = request.POST['Contrasenha']
                nuevo_password = request.POST['Nueva_contrasenha']
                email = request.POST['email']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                telefono = request.POST['telefono']
                direccion = request.POST['direccion']
                documento = request.POST['documento']
                if password:
                    if check_password(password, user.password):
                        password = make_password(nuevo_password)
                    else:
                        error = 'Password incorrecto'
                        return render_to_response('editarUsuario.html',{'formulario':formulario,'errors':error,'usuario':usuarioLo}, context_instance=RequestContext(request))

                else:
                    password = user.password


                user.password = password
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                usuario.telefono = telefono
                usuario.direccion = direccion
                usuario.documento = documento

                usuario.save()

                exito = 'El usuario se modifico con exito'
                return render_to_response('editarUsuario.html',{'formulario':formulario,'exito':exito,'usuario':usuarioLo}, context_instance=RequestContext(request))


            except:
                error = 'Error al procesar la entidad'
                return render_to_response('editarUsuario.html',{'formulario':formulario,'errors':error,'usuario':usuarioLo}, context_instance=RequestContext(request))
    else:
        data = {'Nombre_de_Usuario': usuario.user.username, 'Contrasenha': '', 'Nueva_contrasenha': '',
                    'email': usuario.user.email, 'first_name': usuario.user.first_name, 'last_name': usuario.user.last_name,
                    'telefono' : usuario.telefono,'direccion' : usuario.direccion, 'documento' : usuario.documento }
        formulario = UsuarioEditarForm(data)
    return render_to_response('editarUsuario.html', {'formulario': formulario,'usuario':usuarioLo}, context_instance=RequestContext(request))