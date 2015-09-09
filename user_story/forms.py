from django import forms
from django.forms import ModelMultipleChoiceField
from models import UserStory, Flujouserstory


class MyModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s -- orden: %d" % (obj.nombre, obj.orden)


class UserStoryCreateForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos User Story
    en la base de datos.
    """
    class Meta:
        model = UserStory
        fields = ['nombre', 'descripcion', 'fecha_creacion', 'valor_negocio', 'valor_tecnico', 'prioridad', 'tipo',
                  'autor', 'estado_scrum']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User Story without database save")
        user_story = super(UserStoryCreateForm, self).save(commit=True)

        return user_story


class UserStoryFlujoForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos Estados de User Story
    en la base de datos.
    """
    class Meta:
        model = Flujouserstory
        fields = ['actividad', 'user_story', 'estado_kamban']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create Estate Kanbam of User Story without database save")
        flujo_user_story = super(UserStoryFlujoForm, self).save(commit=True)

        return flujo_user_story
