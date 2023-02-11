from django.db import models as M
from django.db.models import Model
from psqlextra.manager import PostgresManager

class Curso( Model ):

	nombre = M.CharField(max_length=50)
	horario = M.CharField(max_length=50)
	fechaInicio = M.DateTimeField()
	fechaFin = M.DateTimeField()
	numeroEstudiantes = M.IntegerField()
 
 
class Estudiante( Model ):

	nombre = M.CharField(max_length=50)
	apellido = M.CharField(max_length=50)
	edad = M.IntegerField()
	correo = M.EmailField(max_length=254 )
	# cursos = M.ArrayField(models.models.IntegerField())
 
	def toJson( self ):
     
		data = {}
		data["_id"] = self.id
		data["nombre"] = self.nombre
		data["apellido"] = self.apellido
		data["edad"] = self.edad
		data["correo"] = self.correo
  
		return data
