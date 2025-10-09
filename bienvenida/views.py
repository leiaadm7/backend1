from django.http import HttpResponse

def inicio(request):
    nombre = "Leia Donoso"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")