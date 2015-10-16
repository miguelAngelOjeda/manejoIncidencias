from django import forms
from django.forms import ModelMultipleChoiceField
from models import Grupo
from django.contrib.auth.models import User



class GrupoForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos Grupos
    en la base de datos.
    """
    usuarios = ModelMultipleChoiceField(User.objects.all(),
            widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = Grupo
        fields = ['nombre', 'usuarios']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create grupo without database save")
        grupo = super(GrupoForm, self).save(commit=True)

        return grupo


