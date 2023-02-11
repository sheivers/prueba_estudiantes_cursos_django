from django.urls import path

from .views import home

from gestionUsuarios.views import usuariosApi
from gestionCursos.views import cursosApi

urlpatterns = [
    
    path("", home, name="home",),
    
    path("usuarios/", usuariosApi, name="usuarios" ),
    path("cursos/", cursosApi, name="cursos" ),
    
]