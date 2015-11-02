from django.db import models
import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from proyecto.models import Proyecto


class Sprint(models.Model):
    """
    Clase Sprint.
    Crea el formulario para los Sprint para cada instancia de Sprint,
    el cual define los campos nombre, duracion,estado, flujos y proyecto.
    """
    ESTADO_SPRINT = (
        ('No iniciado', 'No iniciado'),
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
    )
    nombre = models.CharField(max_length=15, null=True)
    duracion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)], default=0, null=True)
    estado = models.CharField(max_length=15, choices=ESTADO_SPRINT, default='No iniciado', null=True)
    proyecto = models.ForeignKey(Proyecto, null=True, related_name='proyecto_sprint')
    fecha_inicio = models.DateField(default=datetime.date.today(), null=True)
    fecha_fin = models.DateField(default=datetime.date.today(), null=True)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('sprints', kwargs={'pk': self.pk})

