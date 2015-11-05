# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15, null=True)),
                ('duracion', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('estado', models.CharField(default=b'No iniciado', max_length=15, null=True, choices=[(b'No iniciado', b'No iniciado'), (b'Activo', b'Activo'), (b'Finalizado', b'Finalizado')])),
                ('fecha_inicio', models.DateField(default=datetime.date(2015, 10, 30), null=True)),
                ('fecha_fin', models.DateField(default=datetime.date(2015, 10, 30), null=True)),
                ('proyecto', models.ForeignKey(related_name='proyecto_sprint', to='proyecto.Proyecto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
