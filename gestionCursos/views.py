from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from usuariostest.models import ( Respuesta, parametros )
from gestionCursos.models import Curso

def cursosApi(request):
    
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

