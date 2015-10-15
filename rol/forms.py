from django import forms
from django.forms import ModelMultipleChoiceField
from models import Rol




class RolForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos User Story
    en la base de datos.
    """
    class Meta:
        model = Rol
        fields = ['rol', 'proyecto', 'usuario']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create Rol without database save")
        rol = super(RolForm, self).save(commit=True)

        return rol


