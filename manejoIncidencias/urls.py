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
	url(r'^$','login.views.ingresar'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}),
    url(r'^gestion/$','login.views.home'),
    url(r'^usuarios/$','usuario.views.usuarios'),
    url(r'^usuario/nuevo$','usuario.views.nuevo_usuario'),
    url(r'^gestion/salir/$','login.views.cerrar'),
    url(r'^proyectos/$','proyecto.views.proyectos'),
    url(r'^proyecto/nuevo$','proyecto.views.nuevo_proyecto'),
)