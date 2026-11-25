# pedidos/urls.py
from django.urls import path

from pedidos import views

app_name = "pedidos"

urlpatterns = [
    path("", views.home, name="home"),

    path("CategoriaPlatos/", views.CategoriaPlato_list, name="CategoriaPlato_list"),
    path("CategoriaPlatos/nueva/", views.CategoriaPlato_create, name="CategoriaPlato_create"),
    path("CategoriaPlatos/<int:pk>/", views.CategoriaPlato_detail, name="CategoriaPlato_detail"),
    path("CategoriaPlatos/<int:pk>/editar/", views.CategoriaPlato_update, name="CategoriaPlato_update"),
    path("CategoriaPlatos/<int:pk>/borrar/", views.CategoriaPlato_delete, name="CategoriaPlato_delete"),

    path("Platos/", views.Plato_list, name="Plato_list"),
    path("Platos/nueva/", views.Plato_create, name="Plato_create"),
    path("Platos/<int:pk>/", views.Plato_detail, name="Plato_detail"),
    path("Platos/<int:pk>/editar/", views.Plato_update, name="Plato_update"),
    path("Platos/<int:pk>/borrar/", views.Plato_delete, name="Plato_delete"),
]