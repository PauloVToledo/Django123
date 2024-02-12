# la función include espera que tengamos una variale urlpatterns en el archivo urls.py de la app que estamos incluyendo.
# se indican patrones de las url que queramos seguir

# quiero que solamente me exponga la ruta productos, para que cuando ingrese a esa ruta me ejecute la función.
from django.urls import path
from . import views

# from . es la carpeta en la cual yo me encuentro.


# app_name es convención de django para que no haya conflictos entre las rutas de diferentes aplicaciones
app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("formulario", views.formulario, name="formulario"),
    path("<int:producto_id>", views.detalle, name="detalle"),
]  # siempre es bueno colocar el nombre de la aplicación con la que estamos trabajando, name.
# a medida que agregue más rutas todas estas deben ir incluyendo producto_nombre.

# para referenciar una ruta es mejor usar el nombre de la ruta en vez de la ruta misma
# el argumento de name es indispensable para crear rutas en django
