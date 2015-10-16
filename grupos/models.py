from django.db import models

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class Grupo(models.Model):
    """
    Clase Grupo.
    Crea el formulario para los grupos para cada instancia de Proyecto,
    el cual define los campos nombre, usuarios .
    """

    nombre = models.CharField(max_length=15)
    usuarios = models.ManyToManyField(User, null=False)

    def get_absolute_url(self):
        return reverse('grupo', kwargs={'pk': self.pk})