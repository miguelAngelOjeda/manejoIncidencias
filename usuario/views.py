from django.shortcuts import render
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from usuario.models import Usuario
from django.contrib.auth.forms import  AuthenticationForm
from forms import UserCreateForm
# Create your views here.
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios}, context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreateForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreateForm()
    return render_to_response('crear.html',{'formulario':formulario}, context_instance=RequestContext(request))