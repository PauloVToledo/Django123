from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
# se configuran modelos para que aparezcan en el panel de administración.

# para registrar modelo se llama a un método de la clase admin.


# esto permite personalizar el admin.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


class ProductoAdmin(admin.ModelAdmin):
    # 2 opciones, con fields podemos escoger los campos que queremos que se muestren.
    # exclude es para excluir campos.
    exclude = ("creado_en",)
    list_display = ("id", "nombre", "stock", "creado_en")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
# el método mágico de str sirve para solucioanr el problema de que no se vea el
# nombre del producto en el panel de administración.

# ojo, puedo hacer que la fecha se guarde de manera automática.
