from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime
from proyecto.models import Proyecto

# Create your models here.
class Rol(models.Model):
    """
    Clase Proyecto.
    Crea el formulario para los proyectos para cada instancia de Proyecto,
    el cual define los campos codigo, nombre corto y nombre largo, fecha de inicio, fecha de fin, (estado) Cancelado,
    Scrum master, equipo, estado.
    """
    ROL=(
        ('Development', 'Development'),
        ('Product Owner', 'Product Owner'),
    )
    nombre = models.CharField(max_length=15)
    usuario = models.ManyToManyField(User, null=False)
    proyecto = models.ForeignKey(Proyecto, null=True, related_name='proyecto')
    rol = models.CharField(max_length=15, choices=ROL)


    def get_absolute_url(self):
        return reverse('rol', kwargs={'pk': self.pk})