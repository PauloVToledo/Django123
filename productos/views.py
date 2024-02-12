from django.http import Http404, HttpResponse, HttpResponseRedirect

# JsonResponse ya no se usará
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

# Create your views here.
# todas las vistas reciben un request y retornan un response.

# crl + space: autocompletar vscode.

# ahora al ir a ruta productos debería devolver el string hola mundo.


# con esto accedemos a la url de productos.   /productos/
# cuando vimos la librería de requests vimos que podemos acceder  una api mediante los verbos get, post, put/patch, delete.
# get es para listas elementos


# Con index esto es todo lo que necesitamos para que funcione la vista. return solo necesita 3 cosas.
def index(request):
    productos = Producto.objects.all()
    return render(request, "index.html", context={"productos": productos})

    # productos = Producto.objects.filter(puntaje=3)
    # productos = Producto.objects.get(id=1)  # tambien puedo usar pk
    # print(productos)
    # return JsonResponse(list(productos), safe=False)


#  se usa safe=False en la función JsonResponse para indicar que los
# datos que se están convirtiendo a JSON pueden contener objetos que
# no son serializables de forma nativa por defecto.


# puedo devoler un producto en particular, archivos json o html.
# para poder trabajar con json necesito importar la librería de json y devolver un listado de productos. (list)
# se debe usar values también para que devuelva un diccionario de python.

# se puede cambiar por plantilla html, pero para eso se debe importar render.


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)

    return render(request, "detalle.html", context={"producto": producto})


# la forma de mostrar html es mecánica, tiene un request, un nombre de archivo y un diccionario con el contexto.

# hay una funcionalidad de django que envuelve el try except, que es get_object_or_404 en una sola línea.
# eso se puede usar en lugar de try except.


# para mostrar un formulario dentro de una plantilla html, se debe crear un formulario en base a la clase que acabamos de crear.
def formulario(request):
    if request.method == "POST":

        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # save toma el formulario y lo guarda en la base de datos.
            return HttpResponseRedirect(
                "/productos"
            )  # redirige a la lista de productos.
    else:
        form = ProductoForm()

    return render(request, "producto_form.html", {"form": form})


# nuevamente, los return son muy mecánicos.
# y después de crear el formulario, se debe crear una vista para recibir los datos del formulario.
# es muy lógico el proceso de crear un formulario y recibir los datos del formulario.
# se usa post para recibir los datos del formulario.
