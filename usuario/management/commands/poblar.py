from django.shortcuts import get_object_or_404
from flujos.models import Flujo, Actividad, Estado
from proyecto.models import Proyecto

__author__ = 'Admin'
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from usuario.models import Usuario


class Command(BaseCommand):
    args = ''
    help = 'Puebla la Tabla'

    def handle(self, *args, **options):
        # Esta seccion carga la tabla user
        user = User(username="admin", first_name="", last_name="", is_active=True, is_superuser=True, is_staff=True,
                    password="pbkdf2_sha256$20000$ZGh66Ph8BQC7$FsUgs3D0bIDBDK96VuK55vW6DNdf2ayN+U1D6RIz/Vc=",
                    email="ejemplo@gmail.com", date_joined="2015-11-04T02:30:19.739Z")
        user.save()

        user = User(username="jose", first_name="Jose", last_name="Segovia", is_active=True, is_superuser=False,
                    is_staff=False,
                    password="pbkdf2_sha256$20000$dxT8U7ggCJiu$2dTKThhQauOLcIAejN543ewvl+Vf8CHhFHcLSEUdJe4=",
                    email="ejemplo1@gmail.com", date_joined="2015-11-04T02:30:19.739Z")
        user.save()

        user = User(username="miguel", first_name="Miguel", last_name="Ojeda", is_active=True, is_superuser=False,
                    is_staff=False,
                    password="pbkdf2_sha256$20000$fd7lLj4cfvk0$++gygf1i1gwLDKxOj0bmIMM9dJI0tV3IoKYTOCPhJSg=",
                    email="ejemplo2@gmail.com", date_joined="2015-11-04T02:30:19.739Z")
        user.save()

        user = User(username="mario", first_name="Mario", last_name="Pavon", is_active=True, is_superuser=False,
                    is_staff=False,
                    password="pbkdf2_sha256$20000$5rKnELFhnwl8$4+Kg7U6rhnDL1o7tgiFe/PDBWTUFzT9VPbU5i0z/IsE=",
                    email="ejemplo3@gmail.com", date_joined="2015-11-04T02:30:19.739Z")
        user.save()

        # Esta seccion carga la tabla usuario

        user_detail = get_object_or_404(User, pk=1)
        usuario = Usuario(documento="x", telefono="672213", user=user_detail, direccion="Paraguay")
        usuario.save()

        user_detail = get_object_or_404(User, pk=2)
        usuario = Usuario(documento="x", telefono="672213", user=user_detail, direccion="Paraguay")
        usuario.save()

        user_detail = get_object_or_404(User, pk=3)
        usuario = Usuario(documento="x", telefono="672213", user=user_detail, direccion="Paraguay")
        usuario.save()

        # Esta seccion carga la tabla proyecto

        user_detail = get_object_or_404(User, pk=2)
        proyecto = Proyecto(nombre_corto="Desarrollar", fecha_fin="2015-11-10", scrum_master=user_detail,
                            is_active=True,
                            fecha_inicio="2015-11-04", codigo="1", estado="No iniciado", cancelado=False,
                            nombre_largo="Desarrollar Proyecto")
        proyecto.save()

        user_detail = get_object_or_404(User, pk=3)
        proyecto = Proyecto(nombre_corto="Comer", fecha_fin="2015-11-05", scrum_master=user_detail, is_active=True,
                            fecha_inicio="2015-11-04", codigo="2", estado="No iniciado", cancelado=False,
                            nombre_largo="Comer comida saludable")
        proyecto.save()

        # Esta seccion carga la tabla flujo_estado
        estado = Estado(nombre='To do')
        estado.save()
        estado = Estado(nombre='Doing')
        estado.save()
        estado = Estado(nombre='Done')
        estado.save()
        estado = Estado(nombre='To do')
        estado.save()
        estado = Estado(nombre='Doing')
        estado.save()
        estado = Estado(nombre='Done')
        estado.save()
        estado = Estado(nombre='To do')
        estado.save()
        estado = Estado(nombre='Doing')
        estado.save()
        estado = Estado(nombre='Done')
        estado.save()


        # Esta seccion carga la tabla actividades
        estado1 = get_object_or_404(Estado, pk=2)
        estado2 = get_object_or_404(Estado, pk=3)
        estado3 = get_object_or_404(Estado, pk=1)
        actividad = Actividad(nombre="Planificar", estados=[estado1, estado2, estado3], is_active=True, orden=0)

        estado1 = get_object_or_404(Estado, pk=5)
        estado2 = get_object_or_404(Estado, pk=6)
        estado3 = get_object_or_404(Estado, pk=4)
        actividad = Actividad(nombre="Desarrollar", estados=[estado1, estado2, estado3], is_active=True, orden=0)

        estado1 = get_object_or_404(Estado, pk=8)
        estado2 = get_object_or_404(Estado, pk=9)
        estado3 = get_object_or_404(Estado, pk=7)
        actividad = Actividad(nombre="Probar", estados=[estado1, estado2, estado3], is_active=True, orden=0)

        # Esta seccion carga la tabla flujo
        proyecto = get_object_or_404(Proyecto, pk=1)
        flujo = Flujo(descripcion="", nombre="Desarrollar", is_active=True, proyecto=proyecto)