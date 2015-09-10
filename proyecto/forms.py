import itertools

from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from models import Proyecto
from usuario.models import Usuario
import datetime
from django.utils.timezone import get_current_timezone


class ProyectoForm(forms.ModelForm):
    scrum_master = forms.ModelChoiceField(User.objects.exclude(is_staff=True))

    class Meta:
        model = Proyecto
        fields = ['codigo','nombre_corto', 'nombre_largo', 'scrum_master', 'fecha_inicio', 'fecha_fin']

    def clean_fecha_fin(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']
        fecha_fin = self.cleaned_data['fecha_fin']

        if fecha_fin <= fecha_inicio:
            raise forms.ValidationError("La fecha de finalizacion del proyecto debe ser posterior a la de fecha de inicio.")

        return fecha_fin

class ProyectoEditarForm (forms.Form):
    """ Atributos de Proyecto necesarios para el registro en la base de datos
    de un Proyecto a modificar.

    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades
    @author: Miguel Ojeda

    """
    nombre_corto = forms.CharField(widget=forms.TextInput(),max_length=30, required=True, label='Nombre Corto', error_messages={'required': 'Ingrese un nombre de Usuarios', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    nombre_largo = forms.CharField(widget=forms.TextInput(),max_length=30, required=True, label='Nombre Largo')
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    scrum_master = forms.ModelChoiceField(User.objects.exclude(is_staff=True))



