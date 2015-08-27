# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
                ('orden', models.IntegerField(default=0, max_length=10)),
                ('is_active', models.BooleanField(default=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Flujo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('actividades', models.ManyToManyField(to='flujos.Actividad', null=True)),
                ('proyecto', models.ForeignKey(related_name='proyecto_flujo', to='proyecto.Proyecto', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='estados',
            field=models.ManyToManyField(to='flujos.Estado'),
        ),
    ]
