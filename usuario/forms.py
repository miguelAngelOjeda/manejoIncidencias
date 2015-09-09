# coding=utf-8
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from models import Usuario
from views import *
from django.contrib.auth.forms import AdminPasswordChangeForm


class UserCreateForm(UserCreationForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos Usuarios
    en la base de datos.

    @type UserCreationForm: django.contrib.auth.forms
    @ivar UserCreationForm: Se hereda el formulario incorporado en django para la creacion
                            del objeto User, para usar sus funcionalidades
    """
    first_name = forms.CharField(max_length=30, required=True, label='Nombre', error_messages={'required': 'Ingrese un nombre de Usuarios', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    password1 = forms.RegexField(label='Password', regex=r'^[\w.@+-]+$', min_length=5,
                                 widget=forms.PasswordInput,
                                 help_text='Minimo 5 carateres. Letras, digitos y @/./+/-/_ solamente.', error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    password2 = forms.RegexField(label='Password (Confirmacion)', regex=r'^[\w.@+-]+$', min_length=5,
                                 widget=forms.PasswordInput, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    email = forms.EmailField(required=True)
    telefono = forms.RegexField(regex=r'^[\d()+-]+$', max_length=20,
                                help_text='Digitos y + - ( ) solamente.',required=False)
    direccion = forms.CharField(max_length=50,required=False)
    documento = forms.CharField(max_length=10,required=True,error_messages={'required': 'Ingrese Documento', })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("No se puede crear User y Usuario sin guardar en la base de datos")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Usuario(user=user, telefono=self.cleaned_data['telefono'],
                               direccion=self.cleaned_data['direccion'], documento=self.cleaned_data['documento'])
        user_profile.save()
        return user, user_profile


class UsuarioEditarForm (forms.Form):
    """ Atributos de Usuario necesarios para el registro en la base de datos
    de un Usuario a modificar.

    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades
    @author: Andrea Benitez

    """
    first_name = forms.CharField(widget=forms.TextInput(),max_length=30, required=True, label='Nombre', error_messages={'required': 'Ingrese un nombre de Usuarios', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    last_name = forms.CharField(widget=forms.TextInput(),max_length=30, required=True, label='Apellido')
    Contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    Nueva_contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    email = forms.EmailField(widget=forms.TextInput(),required=True)
    telefono = forms.RegexField(widget=forms.TextInput(),regex=r'^[\d()+-]+$', max_length=20,
                                help_text='Digitos y + - ( ) solamente.',required=False)
    direccion = forms.CharField(widget=forms.TextInput(),max_length=50,required=False)
    documento = forms.CharField(widget=forms.TextInput(),max_length=10,required=True,error_messages={'required': 'Ingrese Documento', })

    def clean(self):
        super(forms.Form,self).clean()
        if 'Contrasenha' in self.cleaned_data and 'Confirmar_contrasenha' in self.cleaned_data:
            if self.cleaned_data['Contrasenha'] != self.cleaned_data['Confirmar_contrasenha']:
                self._errors['Contrasenha'] = [u'Las contrasenhas deben coincidir.']
                self._errors['Confirmar_contrasenha'] = [u'Las contrasenhas deben coincidir.']

        return self.cleaned_data

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("No se puede crear User y Usuario sin guardar en la base de datos")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Usuario(user=user, telefono=self.cleaned_data['telefono'],
                               direccion=self.cleaned_data['direccion'], documento=self.cleaned_data['documento'])
        user_profile.save()
        return user, user_profile

class MyPasswordChangeForm(AdminPasswordChangeForm):
    """
    Clase que verifica si la contraseÃ±a cumple los requisitos necesarios.
    @param AdminPasswordChangeForm.
    """
    error_messages = {
        'password_too_short': "El password debe tener al menos 5 carateres.",
        'password_mismatch': "Los dos campos de password no coinciden.",
    }

    def clean_password1(self):
        passwd = self.cleaned_data['password1']
        if passwd and len(passwd) < 5:
            raise forms.ValidationError(
                self.error_messages['password_too_short'],
                code='password_too_short',
            )
        return passwd




