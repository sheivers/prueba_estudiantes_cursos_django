from django.urls import path

from .views import app, index

from estudiantesCursos.views import cursos, estudiantes, eliminarEstudiante, eliminarCurso


urlpatterns = [
    
    path("", index, name="app"),
    path("app/", lambda r: app(r, 'index.html')),
    path("app/<path:resource>", app),

    path("estudiantes/", estudiantes, name="estudiantes" ),
    path("estudiantes/<int:id>/", eliminarEstudiante, name="eliminarEstudiante" ),
    
    path("cursos/", cursos, name="cursos" ),
    path("cursos/<int:id>/", eliminarCurso, name="eliminarCurso" ),
    
]