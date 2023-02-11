from django.urls import path

from .views import home

from estudiantesCursos.views import cursos, estudiantes, eliminarEstudiante, eliminarCurso

urlpatterns = [
    
    path("", home, name="home",),
    
    path("estudiantes/", estudiantes, name="estudiantes" ),
    path("estudiantes/<int:id>/", eliminarEstudiante, name="eliminarEstudiante" ),
    
    path("cursos/", cursos, name="cursos" ),
    path("cursos/<int:id>/", eliminarCurso, name="eliminarCurso" ),
    
]