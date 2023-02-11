from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home(request):
    
    return HttpResponse("Inicio")

