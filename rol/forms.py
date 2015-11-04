from django import forms
from django.forms import ModelMultipleChoiceField
from models import Rol
from django.contrib.auth.models import User



class RolForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos User Story
    en la base de datos.
    """
    usuario = ModelMultipleChoiceField(User.objects.all().exclude(pk=1),
            widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = Rol
        fields = ['rol', 'usuario']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create Rol without database save")
        rol = super(RolForm, self).save(commit=True)

        return rol


