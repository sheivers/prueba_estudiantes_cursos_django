from django.db import models as M
from django.db.models import Model
from psqlextra.manager import PostgresManager

class Usuario( Model ):

	beer = PostgresManager()
 
	nombre = M.CharField(max_length=50)
	apellido = M.CharField(max_length=50)
	edad = M.IntegerField()
	correo = M.EmailField(max_length=254 )
	# cursos = M.ArrayField(models.models.IntegerField())
