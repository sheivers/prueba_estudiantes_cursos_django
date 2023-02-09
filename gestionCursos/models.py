from django.db import models as M
from django.db.models import Model
from psqlextra.manager import PostgresManager

class Curso( Model ):

	nombre = M.CharField(max_length=50)
	horario = M.CharField(max_length=50)
	fechaInicio = M.DateTimeField()
	fechaFin = M.DateTimeField()
	numeroEstudiantes = M.IntegerField()
