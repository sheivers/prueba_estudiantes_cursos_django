from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from usuariostest.models import ( Respuesta, parametros )
from estudiantesCursos.models import ( Curso, Estudiante )


def home(request):
    return JsonResponse(Respuesta(st="0.0").trans() )