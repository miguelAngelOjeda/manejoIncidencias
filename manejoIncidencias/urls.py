"""manejoIncidencias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'login.views.ingresar'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT, }),
                       url(r'^gestion/$', 'login.views.home'),
                       url(r'^usuarios/$', 'usuario.views.usuarios'),
                       url(r'^usuario/delete/(?P<pk_usuario>\d+)$', 'usuario.views.desactivar'),
                       url(r'^usuario/activate/(?P<pk_usuario>\d+)$', 'usuario.views.activar'),
                       url(r'^usuario/visualizar/(?P<pk_usuario>\d+)$', 'usuario.views.consultarUsuario'),
                       url(r'^usuario/editar/(?P<pk_usuario>\d+)$', 'usuario.views.usuarioEditar'),
                       url(r'^usuario/nuevo$', 'usuario.views.nuevo_usuario'),
                       url(r'^gestion/salir/$', 'login.views.cerrar'),
                       url(r'^proyectos/salir/$', 'login.views.cerrar'),
                       url(r'^usuarios/salir/$', 'login.views.cerrar'),
                       url(r'^flujos/salir/$', 'login.views.cerrar'),
                       url(r'^actividades/salir/$', 'login.views.cerrar'),
                       url(r'^userstory/salir/$', 'login.views.cerrar'),
                       url(r'^proyectos/$', 'proyecto.views.proyectos'),
                       url(r'^proyecto/delete/(?P<pk_proyecto>\d+)$', 'proyecto.views.desactivar'),
                       url(r'^proyecto/activate/(?P<pk_proyecto>\d+)$', 'proyecto.views.activar'),
                       url(r'^proyecto/visualizar/(?P<pk_proyecto>\d+)$', 'proyecto.views.consultarProyecto'),
                       url(r'^proyecto/editar/(?P<pk_proyecto>\d+)$', 'proyecto.views.proyectoEditar'),
                       url(r'flujos/$', 'flujos.views.flujos'),
                       url(r'grupos/$', 'rol.views.grupos'),
                       url(r'^roles/usuarios/(?P<pk_rol>\d+)$', 'rol.views.lista_usuarios'),
                       url(r'grupos/crear$', 'rol.views.nuevo_grupo'),
                       url(r'grupo/$', 'grupos.views.grupos_listar'),
                       url(r'grupo/crear$', 'grupos.views.grupo_nuevo'),
                       url(r'^grupos/usuarios/(?P<pk_grupo>\d+)$', 'grupos.views.lista_usuarios'),
                       url(r'actividades/$', 'flujos.views.actividades'),
                       url(r'^flujos/delete/(?P<pk_flujo>\d+)$', 'flujos.views.desactivar'),
                       url(r'^flujos/activate/(?P<pk_flujo>\d+)$', 'flujos.views.activar'),
                       url(r'actividad/crear$', 'flujos.views.nueva_actividad'),
                       url(r'^proyecto/nuevo$', 'proyecto.views.nuevo_proyecto'),
                       url(r'flujo/crear$', 'flujos.views.nuevo_flujo'),
                       url(r'userstory/$', 'user_story.views.lista_user_story'),
                       url(r'^userstory/crear$', 'user_story.views.nuevo_userstory'),
                       url(r'^userstory/cambiarestado/(?P<id_user_story>\d+)$', 'user_story.views.consultar_estado'),
                       url(r'^userstory/estado/$', 'user_story.views.estados'),
                       url(r'sprints/$', 'sprints.views.sprints'),
                       url(r'^sprints/crear$', 'sprints.views.nuevo_sprint'),
                       url(r'^sprints/asignar/(?P<pk_sprints>\d+)/userstory$', 'sprints.views.asignarUserStory'),
                       url(r'^sprints/visualizar/(?P<pk_sprints>\d+)/userstory$', 'sprints.views.visualizarUserStory'),
                       url(r'^asignar/(?P<pk_userStory>\d+)$', 'user_story.views.asignarSprint')
                       )
