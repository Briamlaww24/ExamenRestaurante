# pedidos/views.py
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Prefetch, ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from pedidos.forms import CategoriaPlatoForm, PlatoForm
from pedidos.models import CategoriaPlato, Plato


def home(request):
    """Portada: resume los dos CRUD y enlaza a cada uno."""
    platos_disponibles = Plato.objects.filter(disponible=True)
    contexto = {
        "total_categorias": CategoriaPlato.objects.count(),
        "total_platos": Plato.objects.count(),
        "disponibles": platos_disponibles.count(),
        "ultimos_platos": platos_disponibles.select_related("categoria").order_by(
            "-registrado_en", "-pk"
        )[:5],
        "categorias": CategoriaPlato.objects.prefetch_related(
            Prefetch("platos", queryset=platos_disponibles, to_attr="platos_disponibles")
        ),
    }
    return render(request, "pedidos/home.html", contexto)


# --- CRUD de CategoriaPlato ---------------------------------------------------

def CategoriaPlato_list(request):
    categorias = CategoriaPlato.objects.annotate(total_platos=Count("platos")).order_by("nombre")
    page_obj = Paginator(categorias, 10).get_page(request.GET.get("page"))
    return render(request, "pedidos/CategoriaPlato_list.html", {
        "categorias": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    })


def CategoriaPlato_detail(request, pk):
    categoria = get_object_or_404(CategoriaPlato, pk=pk)
    return render(request, "pedidos/CategoriaPlato_detail.html", {"categoria": categoria})


def CategoriaPlato_create(request):
    if request.method == "POST":
        form = CategoriaPlatoForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect(categoria)
    else:
        form = CategoriaPlatoForm()
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Nueva categoría",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


def CategoriaPlato_update(request, pk):
    categoria = get_object_or_404(CategoriaPlato, pk=pk)
    if request.method == "POST":
        form = CategoriaPlatoForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect(categoria)
    else:
        form = CategoriaPlatoForm(instance=categoria)
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Editar categoría",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


def CategoriaPlato_delete(request, pk):
    categoria = get_object_or_404(CategoriaPlato, pk=pk)
    if request.method == "POST":
        try:
            categoria.delete()
        except ProtectedError:
            messages.error(request, "No se puede eliminar esta categoría porque tiene platos asociados.")
            return redirect(categoria)
        messages.success(request, "Categoría eliminada.")
        return redirect("pedidos:CategoriaPlato_list")
    return render(request, "pedidos/confirm_delete.html", {
        "objeto": categoria,
        "titulo": "¿Borrar esta categoría?",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


# --- CRUD de Plato -------------------------------------------------------

def Plato_list(request):
    platos = Plato.objects.select_related("categoria")
    page_obj = Paginator(platos, 10).get_page(request.GET.get("page"))
    return render(request, "pedidos/Plato_list.html", {
        "platos": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    })


def Plato_detail(request, pk):
    plato = get_object_or_404(Plato.objects.select_related("categoria"), pk=pk)
    return render(request, "pedidos/Plato_detail.html", {"plato": plato})


def Plato_create(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            plato = form.save()
            messages.success(request, "Plato creado exitosamente.")
            return redirect(plato)
    else:
        form = PlatoForm()
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Nuevo plato",
        "volver_url": "pedidos:Plato_list",
    })


def Plato_update(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            messages.success(request, "Plato actualizado exitosamente.")
            return redirect(plato)
    else:
        form = PlatoForm(instance=plato)
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Editar plato",
        "volver_url": "pedidos:Plato_list",
    })


def Plato_delete(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        plato.delete()
        messages.success(request, "Plato eliminado.")
        return redirect("pedidos:Plato_list")
    return render(request, "pedidos/confirm_delete.html", {
        "objeto": plato,
        "titulo": "¿Borrar este plato?",
        "volver_url": "pedidos:Plato_list",
    })
