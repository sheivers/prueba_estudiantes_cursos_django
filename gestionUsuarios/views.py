import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from gestionUsuarios.models import Usuario
from usuariostest.models import ( Respuesta , parametros )


def usuariosApi(request):
    
    data = {}
    
    # Obtener cursos
    if( request.method == "GET"):
        
        try:
            datoDb = Usuario.objects.filter(nombre="Andres")
            data["estudiantes"] = datoDb
            return JsonResponse(Respuesta(st="0.0").trans() )
    
        except Exception as e:
            print(e)
            return JsonResponse(Respuesta(st="1.0").trans() )
    
    
    
    
    # Agregar/actualizar curso
    if( request.method == "PUT"):
         # Verificamos los parametros
        try:
            
            jsondata = json.loads(request.body)
            requeridas = ["nombre","apellido","correo","edad"]
            opcionales = ["id","cursos"]
            jsondata = parametros( jsondata, requeridas, opcionales, False )

        except:
           return JsonResponse(Respuesta(st="2.0").trans() )

        try:
            datoDb = Usuario(
                nombre=jsondata["nombre"],
                apellido=jsondata["apellido"],
                correo=jsondata["correo"],
                # edad=jsondata["edad"],
                # cursos= jsondata["cursos"],
            )
            datoDb.save()
            # data["estudiante"] = json.dumps(datoDb.__dict__)
            
            return JsonResponse(Respuesta(st="0.0",data=data).trans() )
        
        except Exception as e:
            print(e)
            return JsonResponse(Respuesta(st="1.0").trans() )
        
        
        

    else:
        return JsonResponse(Respuesta(st="3.0").trans() )



