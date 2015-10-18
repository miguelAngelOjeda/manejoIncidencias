from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from proyecto.models import Proyecto

class Estado(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

    class Meta:
        ordering = ('nombre',)

class Actividad(models.Model):
    nombre = models.CharField(max_length=15)
    estados = models.ManyToManyField(Estado)
    orden = models.IntegerField(max_length=10, default=0)
    is_active = models.BooleanField(default = True, editable=False)

    def __unicode__(self):
        return self.nombre

class Flujo(models.Model):
    nombre = models.CharField(max_length=15)
    actividades = models.ManyToManyField(Actividad, null=True)
    descripcion = models.CharField(max_length = 150)
    is_active = models.BooleanField(default = True, editable=False)
    proyecto = models.ForeignKey(Proyecto, null=True, related_name='proyecto_flujo')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('flujos', kwargs={'pk': self.pk})



