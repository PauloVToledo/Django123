"""django123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

# include recibe como parametro un string que es la ruta de la app que queremos incluir.


# para agregar página de inicio. esta ruta no se agrega en la carpeta productos
# es la única excepción.
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("admin/", admin.site.urls),
    path("productos/", include("productos.urls")),
]
# no se coloca la extension de la app, solo el nombre de la app.
