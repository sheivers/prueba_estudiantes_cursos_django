from django.views.static import serve
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLUTTER_WEB_APP = os.path.join(BASE_DIR, 'app')

def app(request, resource):
    return serve(request, resource, FLUTTER_WEB_APP)
