from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html")
    # se coloca el nombre del archivo html que se encuentra en la carpeta templates
    # aquí no es necesario colocar argumentos.
