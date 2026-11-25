# pedidos/forms.py
from django import forms

from .models import CategoriaPlato, Plato


class CategoriaPlatoForm(forms.ModelForm):
    class Meta:
        model = CategoriaPlato
        fields = ["nombre", "descripcion"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
        }


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ["categoria", "nombre", "descripcion", "precio", "tipo_servicio", "disponible"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
            "precio": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }
