from django.apps import AppConfig

# si me muestran error las importaciones es porque debo usar el interprete adecuado.


class ProductosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "productos"
