# el nombre del archivo también es una convención

# si queremos que un usuario cree un producto.
# django puede escribir formularios en base a los modelos que ya tenemos.
# Model Form es una dependencia que usa los productos y devuelve un formulario.

from . import models
from django.forms import ModelForm


class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "stock", "puntaje", "categoria"]


# se indican los campos que queremos que use.
# se requiere instalar django forms en settings.py
