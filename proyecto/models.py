#!/usr/bin/env python
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime


# Create your models here.
class Proyecto(models.Model):
    """
    Clase Proyecto.
    Crea el formulario para los proyectos para cada instancia de Proyecto,
    el cual define los campos codigo, nombre corto y nombre largo, fecha de inicio, fecha de fin, (estado) Cancelado,
    Scrum master, equipo, estado.
    """
    ESTADOS_PROYECTO=(
        ('No inciado', 'No inciado'),
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
    )
    codigo = models.SlugField(max_length=4, unique=True, null=True)
    nombre_corto = models.CharField(max_length=15)
    nombre_largo = models.CharField(max_length=40)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    is_active = models.BooleanField(default=True)
    cancelado = models.BooleanField(default=False)
    scrum_master = models.OneToOneField(User, null=True, related_name='scrum_master')
    equipo = models.ManyToManyField(User, null=True)
    estado = models.CharField(max_length=15, choices=ESTADOS_PROYECTO, default='No iniciado')

    def __unicode__(self):
        return self.nombre_corto

    def get_absolute_url(self):
        return reverse('proyectos', kwargs={'pk': self.pk})