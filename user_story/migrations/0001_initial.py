# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flujouserstory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_kamban', models.CharField(default=b'To Do', max_length=20, choices=[(b'To Do', b'To Do'), (b'Doing', b'Doing'), (b'Done', b'Done')])),
                ('actividad', models.ForeignKey(related_name='user_story_actividad', to='flujos.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('valor_negocio', models.IntegerField(default=0)),
                ('valor_tecnico', models.IntegerField(default=0)),
                ('prioridad', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=20)),
                ('estado_scrum', models.CharField(default=b'Nuevo', max_length=20, choices=[(b'Cancelado', b'Cancelado'), (b'Finalizado', b'Finalizado'), (b'En Proceso', b'En Proceso'), (b'Nuevo', b'Nuevo')])),
                ('autor', models.OneToOneField(related_name='autor', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='flujouserstory',
            name='user_story',
            field=models.ForeignKey(related_name='user_story_flujo', to='user_story.UserStory'),
        ),
    ]
