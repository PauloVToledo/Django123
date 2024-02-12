from django.utils import timezone
from django.db import models

# Create your models here.
# permite definir clases que representan tablas en la base de datos.
# así se trabaja con python y no con sql o el gestor de base de datos que queramos usar.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    # es importante que el método mágico devuelva el nombre para que se muestre en el html


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: elimina los productos si se elimina la categoria.
    # Protect: no se puede eliminar la categoria si hay productos asociados.
    # Restrict: no se puede eliminar la categoria si hay productos asociados.
    # SetNull: pone el campo categoria en null si se elimina la categoria.
    # SetDefault: pone el campo categoria en el valor por defecto si se elimina la categoria.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # referencia a la tabla categoria
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    # quieroq que la asignación de la fecha sea automática.
    # se pasa la referencia, no se ejecuta the function now.


# ahora que creamos los modelos debemos actualziar la base de datos.
# Migración: es un paso a paso de los cambios que se hacen en la base de datos.

# se generan en la terminal.
# you have 18 apps without migrations; run 'python manage.py makemigrations' to see them.
# python manage.py makemigrations.
# python manage.py migrate.
