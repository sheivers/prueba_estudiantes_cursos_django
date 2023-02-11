import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from usuariostest.models import ( Respuesta, parametros )
from estudiantesCursos.models import ( Curso, Estudiante )


def cursos(request):
    
    # Obtener cursos
    if( request.method == "GET"):
        
        try:
            
            curso = Curso(nombre="Nombre del curos")
            return JsonResponse(Respuesta(st="0.0").trans() )
        except:
            return JsonResponse(Respuesta(st="1.0").trans() )
        
        
        
    # Agregar/actualizar curso
    if( request.method == "PUT"):
        
        # Verificamos los parametros
        try:
            requeridas = ["nombre","correo","edad","apellido"]
            opcionales = ["cursos"]
            jsondata = parametros( jsondata, requeridas, opcionales, False )

        except:
           return JsonResponse(Respuesta(st="2.0").trans() )


        try:
            curso = Curso(
                nombre=jsondata["nombre"],
                apellido=jsondata["apellido"],
                correo=jsondata["correo"],
                edad=jsondata["edad"],
                # cursos= jsondata["cursos"],
            )
            curso.save()
        
            return JsonResponse(Respuesta(st="0.0").trans() )
        
        except Exception as e:
            print(e)
            return JsonResponse(Respuesta(st="1.0").trans() )
        
    

    else:
        return JsonResponse(Respuesta(st="3.0").trans() )


    
def eliminarCurso( request, id ):
           
    if( request.method == "DELETE"):
         return JsonResponse(Respuesta(st="0.0").trans() )
        
    else:
        return JsonResponse(Respuesta(st="3.0").trans() )












def estudiantes(request):
    
    data = {}
    
    # Obtener cursos
    if( request.method == "GET"):
        
        try:
            listaEstudiantes = []
            cursor = Estudiante.objects.filter()

            for est in cursor:
                listaEstudiantes.append( est.toJson() )
            
            data["estudiantes"] = listaEstudiantes
            return JsonResponse(Respuesta(st="0.0",data=data).trans() )
    
        except Exception as e:
            print(e)
            return JsonResponse(Respuesta(st="1.0").trans() )
    
    
    
    
    # Agregar/actualizar curso
    elif( request.method == "PUT"):
         # Verificamos los parametros
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
                
            data["estudiante"] = datoDb.toJson()
            
            return JsonResponse(Respuesta(st="0.0",data=data).trans() )
        
        except Exception as e:
            print(e)
            return JsonResponse(Respuesta(st="1.0",ms="Información incorrecta").trans() )
        
    else:
        return JsonResponse(Respuesta(st="3.0").trans() )



def eliminarEstudiante( request, id ):
           
    if( request.method == "DELETE"):
         return JsonResponse(Respuesta(st="0.0").trans() )
        
    else:
        return JsonResponse(Respuesta(st="3.0").trans() )
    

