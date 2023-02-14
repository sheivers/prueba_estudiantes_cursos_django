from django.db import models as M
from django.db.models import Model
from psqlextra.manager import PostgresManager

class Curso( Model ):

	nombre = M.CharField(max_length=50)
	horario = M.CharField(max_length=50)
	fechaInicio = M.DateTimeField()
	fechaFin = M.DateTimeField()

	def toJson( self ):
		data = {}
		data["_id"] = self.id
		data["nombre"] = self.nombre
		data["horario"] = self.horario
		data["fechaInicio"] = self.fechaInicio
		data["fechaFin"] = self.fechaFin

		# Numero de estudiantes
		estudiantes_count = Estudiante.objects.filter(cursos__id=self.id ).count()

		data["numero"] = estudiantes_count
		return data
 
 
 
class Estudiante( Model ):

	nombre = M.CharField( max_length=50 )
	apellido = M.CharField( max_length=50 )
	edad = M.IntegerField()
	correo = M.EmailField( max_length=254, unique=True )
	cursos = M.ManyToManyField(Curso)
 
	def toJson( self ):
		data = {}
		data["_id"] = self.id
		data["nombre"] = self.nombre
		data["apellido"] = self.apellido
		data["edad"] = self.edad
		data["correo"] = self.correo
		data["cursos"] = [ {"nombre":curso.nombre, "_id":curso.id} for curso in self.cursos.all()]
  
		return data
