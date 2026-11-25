# pedidos/views.py
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from pedidos.forms import CategoriaPlatoForm, PlatoForm
from pedidos.models import CategoriaPlato, Plato


def home(request):
    """Portada: resume los dos CRUD y enlaza a cada uno."""
    contexto = {
        "Total_Categorias": CategoriaPlato.objects.count(),
        "Total_Platos": Plato.objects.count(),
        "Disponibles": Plato.objects.filter(disponible=True).count(),
        "Ultimos_Platos": Plato.objects.select_related("CategoriaPlato").order_by("-registrado_en")[:5],
        "CategoriaPlatos": CategoriaPlato.objects.all(),
    }
    return render(request, "pedidos/home.html", contexto)


# --- CRUD de CategoriaPlato ---------------------------------------------------

def CategoriaPlato_list(request):
    CategoriaPlatos = CategoriaPlato.objects.all()
    page_obj = Paginator(CategoriaPlatos, 10).get_page(request.GET.get("page"))
    return render(request, "pedidos/CategoriaPlato_list.html", {
        "CategoriaPlatos": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    })


def CategoriaPlato_detail(request, pk):
    CategoriaPlato = get_object_or_404(CategoriaPlato, pk=pk)
    return render(request, "pedidos/CategoriaPlato_detail.html", {"CategoriaPlato": CategoriaPlato})


def CategoriaPlato_create(request):
    if request.method == "POST":
        form = CategoriaPlatoForm(request.POST)
        if form.is_valid():
            CategoriaPlato = form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect(CategoriaPlato)
    else:
        form = CategoriaPlatoForm()
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Nueva categoría",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


def CategoriaPlato_update(request, pk):
    CategoriaPlato = get_object_or_404(CategoriaPlato, pk=pk)
    if request.method == "POST":
        form = CategoriaPlatoForm(request.POST, instance=CategoriaPlato)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect(CategoriaPlato)
    else:
        form = CategoriaPlatoForm(instance=CategoriaPlato)
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Editar categoría",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


def CategoriaPlato_delete(request, pk):
    CategoriaPlato = get_object_or_404(CategoriaPlato, pk=pk)
    if request.method == "POST":
        CategoriaPlato.delete()
        messages.success(request, "Categoría eliminada.")
        return redirect("pedidos:CategoriaPlato_list")
    return render(request, "pedidos/confirm_delete.html", {
        "objeto": CategoriaPlato,
        "titulo": "¿Borrar esta categoría?",
        "volver_url": "pedidos:CategoriaPlato_list",
    })


# --- CRUD de Plato -------------------------------------------------------

def Plato_list(request):
    Platos = Plato.objects.select_related("CategoriaPlato")
    page_obj = Paginator(Platos, 10).get_page(request.GET.get("page"))
    return render(request, "pedidos/Plato_list.html", {
        "Platos": page_obj,
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
    })


def Plato_detail(request, pk):
    Plato = get_object_or_404(Plato.objects.select_related("CategoriaPlato"), pk=pk)
    return render(request, "pedidos/Plato_detail.html", {"Plato": Plato})


def Plato_create(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            Plato = form.save()
            messages.success(request, "Plato creada exitosamente.")
            return redirect(Plato)
    else:
        form = PlatoForm()
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Nueva Plato",
        "volver_url": "pedidos:Plato_list",
    })


def Plato_update(request, pk):
    Plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=Plato)
        if form.is_valid():
            form.save()
            messages.success(request, "Plato actualizada exitosamente.")
            return redirect(Plato)
    else:
        form = PlatoForm(instance=Plato)
    return render(request, "pedidos/form.html", {
        "form": form,
        "titulo": "Editar Plato",
        "volver_url": "pedidos:Plato_list",
    })


def Plato_delete(request, pk):
    Plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        Plato.delete()
        messages.success(request, "Plato eliminado.")
        return redirect("pedidos:Plato_list")
    return render(request, "pedidos/confirm_delete.html", {
        "objeto": Plato,
        "titulo": "¿Borrar esta Plato?",
        "volver_url": "pedidos:Plato_list",
    })