#!/usr/bin/env python
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from flujos.models import Actividad
from proyecto.models import Proyecto
from usuario.models import Usuario
from sprints.models import Sprint
from flujos.models import Flujo
import datetime


# Create your models here.


class UserStory(models.Model):
    """
    Clase UserStory.
    Los campos definidos son nombre, descripcion, fecha de creacion, valor de negocio, valor tecnico, prioridad, tipo,
    autor y estados SCRUM.
    """
    ESTADOS_SCRUM = (
        ('Cancelado', 'Cancelado'),
        ('Finalizado', 'Finalizado'),
        ('En Proceso', 'En Proceso'),
        ('Nuevo', 'Nuevo')
    )
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    fecha_creacion = models.DateField(default=datetime.date.today)
    valor_de_negocio = models.IntegerField(max_length=2, help_text='Introduzca un valor de negocio (1 al 10)', null = False)
    valor_tecnico = models.IntegerField(default=0)
    duracion_horas = models.IntegerField(max_length=4,  null=False)
    duracion_horas_en_sprint = models.IntegerField(max_length=4, help_text='duracion de horas en el sprint', null=True, blank=True)
    prioridad = models.IntegerField(max_length=3, help_text= 'Introduzca alguna prioridad para el User Stories', null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    tipo = models.CharField(max_length=20)
    autor = models.ForeignKey(Usuario, null=True, related_name='scrum_master')
    proyecto = models.ForeignKey(Proyecto, null=False)
    estado_scrum = models.CharField(max_length=20, choices=ESTADOS_SCRUM, default='Nuevo')
    flujo = models.ForeignKey(Flujo, null=True, related_name='flujo')
    sprint = models.ForeignKey(Sprint, null=True, related_name='sprint_user_story')

    def __unicode__(self):
        return self.nombre

    def __get_absolute_url(self):
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

