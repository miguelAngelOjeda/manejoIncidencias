import itertools

from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from models import Proyecto
from usuario.models import Usuario


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

