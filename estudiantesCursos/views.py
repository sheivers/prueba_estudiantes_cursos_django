import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from usuariostest.models import ( Respuesta, parametros )
from estudiantesCursos.models import ( Curso, Estudiante )

from django.utils import timezone
from django.db.models import Count


def cursos(request):
	
	data = {}
	   
	# Obtener estudiantes
	if( request.method == "GET"):
		
		try:
			
			top = request.GET.get("top",False)
			cursos = []
			listaData = []
   
			if( top ):
				
				six_months_ago = timezone.now() - timezone.timedelta(days=180)

				cursos = (Curso.objects.filter(fechaInicio__gte=six_months_ago)
					.annotate(num_students=Count('estudiante'))
					.order_by('-num_students')[:3])
			else:
				
				cursos = Curso.objects.filter()

			for info in cursos:
				listaData.append( info.toJson() )
			
			data["cursos"] = listaData
			return JsonResponse(Respuesta(st="0.0",data=data).trans() )
	
		except Exception as e:
			print(e)
			return JsonResponse(Respuesta(st="1.0").trans() )
		
		
		
	# Agregar/actualizar estudiante
	elif( request.method == "PUT"):
		
		try:
			jsondata = json.loads(request.body)
			requeridas = ["nombre","horario","fechaInicio","fechaFin"]
			opcionales = ["_id"]
			id = jsondata.get("_id",None)
			jsondata = parametros( jsondata, requeridas, opcionales, False )

		except Exception as e:
		   return JsonResponse(Respuesta(st="2.0").trans() )

		try:
			
			datoDb, created = Curso.objects.update_or_create(
				id=id,
				defaults={
					"nombre": jsondata["nombre"],
					"horario": jsondata["horario"],
					"fechaInicio": jsondata["fechaInicio"],
					"fechaFin": jsondata["fechaFin"],
				}
			)
				
			data["curso"] = datoDb.toJson()
			
			return JsonResponse(Respuesta(st="0.0",data=data).trans() )
		
		except Exception as e:
			print(e)
			return JsonResponse(Respuesta(st="1.0",ms="Información incorrecta").trans() )
		
	else:
		return JsonResponse(Respuesta(st="3.0").trans() )


	
def eliminarCurso( request, id ):
	
	if( request.method == "DELETE"):
		 
		try:

			estudiantes = Estudiante.objects.filter(cursos__id=id)

			if len(estudiantes) == 0:
				curso = Curso.objects.get(id=id)
				curso.delete()
				return JsonResponse(Respuesta(st="0.0").trans() )
			else:
				return JsonResponse(Respuesta(st="1.0",ms="Aun hay estudiantes asociados").trans() )
		except:
			return JsonResponse(Respuesta(st="1.0").trans() )
	
	else:
		return JsonResponse(Respuesta(st="3.0").trans() )












def estudiantes(request):
	
	data = {}
	
	# Obtener estudiantes
	if( request.method == "GET"):
		
		try:
			listaData = []
			cursor = Estudiante.objects.filter().order_by('id')


			for info in cursor:
				listaData.append( info.toJson() )
			
			data["estudiantes"] = listaData
			return JsonResponse(Respuesta(st="0.0",data=data).trans() )
	
		except Exception as e:
			print(e)
			return JsonResponse(Respuesta(st="1.0").trans() )
	
	
	
	
	# Agregar/actualizar estudiante
	elif( request.method == "PUT"):
		
		
		try:
			
			jsondata = json.loads(request.body)
			requeridas = ["nombre","apellido","correo","edad"]
			opcionales = ["id","cursos"]
			id = jsondata.get("_id",None)
			jsondata = parametros( jsondata, requeridas, opcionales, False )

		except:
		   return JsonResponse(Respuesta(st="2.0").trans() )
		
		try:
			
			datoDb, created = Estudiante.objects.update_or_create(
				id=id,
				defaults={
					"nombre": jsondata["nombre"],
					"apellido": jsondata["apellido"],
					"correo": jsondata["correo"],
					"edad": jsondata["edad"],
				}
			)
			
			cursos = jsondata.get("cursos",[])
			cursos = [ Curso.objects.get(id=curso_id) for curso_id in cursos ]
			datoDb.cursos.set(cursos)
				
			data["estudiante"] = datoDb.toJson()
			
			return JsonResponse(Respuesta(st="0.0",data=data).trans() )
		
		except Exception as e:
			print(e)
			return JsonResponse(Respuesta(st="1.0",ms="Información incorrecta").trans() )
		
	else:
		return JsonResponse(Respuesta(st="3.0").trans() )



def eliminarEstudiante( request, id ):
	
	if( request.method == "DELETE"):
		try:
			estudiante = Estudiante.objects.get(id=id)
			estudiante.delete()
			return JsonResponse(Respuesta(st="0.0").trans() )
		except:
			return JsonResponse(Respuesta(st="1.0").trans() )
	else:
		return JsonResponse(Respuesta(st="3.0").trans() )

	

