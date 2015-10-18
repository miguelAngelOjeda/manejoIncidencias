#!/usr/bin/env python
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from flujos.models import Actividad
from usuario.models import Usuario
import datetime


# Create your models here.


class UserStory(models.Model):
    """
    Clase UserStory.
    Los campos definidos son nombre, descripcion, fecha de creacion, valor de negocio, valor tecnico, prioridad, tipo,
    autor y estados SCRUM.
    """
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    fecha_creacion = models.DateField(default=datetime.date.today)
    valor_negocio = models.IntegerField(default=0)
    valor_tecnico = models.IntegerField(default=0)
    prioridad = models.IntegerField(default=0)
    tipo = models.CharField(max_length=20)
    autor = models.OneToOneField(User, null=True, related_name='autor')
    ESTADOS_SCRUM = (
        ('Cancelado', 'Cancelado'),
        ('Finalizado', 'Finalizado'),
        ('En Proceso', 'En Proceso'),
        ('Nuevo', 'Nuevo')
    )
    estado_scrum = models.CharField(max_length=20, choices=ESTADOS_SCRUM, default='Nuevo')

    def __unicode__(self):
        """


            @return: @rtype:
            """
        return self.nombre

    def __get_absolute_url(self):
        """


            @return: @rtype:
            """
        return reverse('user_story', kwargs={'pk': self.pk})


class Flujouserstory(models.Model):
    """
    Clase FlujouserStory.
    Relacionado a la clase UserStory y la clase Actividad.
    Los campos definidos son actividad, user story y estados kanbam.
    """
    actividad = models.ForeignKey(Actividad, related_name='user_story_actividad')
    user_story = models.ForeignKey(UserStory, related_name='user_story_flujo')
    ESTADOS_KAMBAN = (
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done')
    )
    estado_kamban = models.CharField(max_length=20, choices=ESTADOS_KAMBAN, default='To Do')

    def __unicode__(self):
        return self.actividad


class UserStoryHoars(models.Model):
    user_story = models.OneToOneField(UserStory, null=False, related_name='user_story_hrs')
    horas_estimadas = models.IntegerField(default=0)
    horas_trabajadas = models.IntegerField(default=0)
