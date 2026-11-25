# pedidos/admin.py
from django.contrib import admin

from pedidos.models import CategoriaPlato, Plato


@admin.register(CategoriaPlato)
class CategoriaPlatoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "tipo_servicio", "precio", "disponible")
    list_filter = ("categoria", "tipo_servicio", "disponible")
    search_fields = ("nombre", "descripcion")
