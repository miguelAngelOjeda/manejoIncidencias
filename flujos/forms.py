from django import forms
from django.forms import ModelMultipleChoiceField
from models import Flujo, Actividad, Estado
from proyecto.models import Proyecto


class MyModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s -- orden: %d" % (obj.nombre, obj.orden)


class FlujoCreateForm(forms.ModelForm):
    # actividades = ModelMultipleChoiceField(Actividad.objects.all(),
    #                                        widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = Flujo
        fields = ['nombre', 'descripcion', 'proyecto']


class ActividadCreateForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create Actividad without database save")
        actividad = super(ActividadCreateForm, self).save(commit=True)

        estado1 = Estado(nombre="To do")
        estado1.save()
        estado2 = Estado(nombre="Doing")
        estado2.save()
        estado3 = Estado(nombre="Done")
        estado3.save()

        actividad.estados.add(estado1)
        actividad.estados.add(estado2)
        actividad.estados.add(estado3)

        actividad.save()

        return actividad


# class AsignarFlujoProyectoForm(forms.ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         context = super(AsignarFlujoProyectoForm, self).__init__(*args, **kwargs)
#         proyecto = Proyecto.objects.get(pk=kwargs['instance'].pk)
#         flujos_actuales = Flujo.objects.filter(proyecto=proyecto)
#
#         self.fields['flujos'] = forms.ModelMultipleChoiceField(Flujo.objects.all().order_by('id'),
#                                                                widget=forms.CheckboxSelectMultiple, required=True)
#
#         dic = {}
#         for arr in flujos_actuales:
#             dic[arr.pk] = arr
#         self.fields['flujos'].initial = dic
#
#     codigo = forms.CharField(widget=forms.HiddenInput(), required=True)
#
#     class Meta:
#         model = Proyecto
#         fields = ['codigo']
#
#     def save(self, commit=True):
#         if not commit:
#             raise NotImplementedError("Can't create Flujo without database save")
#
#         proyecto = super(AsignarFlujoProyectoForm, self).save(commit=True)
#
#         lista_completa = Flujo.objects.all()
#         print "self %s" % self.cleaned_data['flujos']
#         for flujo in self.cleaned_data['flujos']:
#             flujo.proyecto = proyecto
#             flujo.save()
#             for f in lista_completa:
#                 if f not in self.cleaned_data['flujos']:
#                     f.proyecto = None
#                     f.save()
#
#         return proyecto
