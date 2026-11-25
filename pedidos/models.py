# pedidos/models.py
from django.db import models
from django.urls import reverse


class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField("descripción", blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("pedidos:CategoriaPlato_detail", kwargs={"pk": self.pk})


class Plato(models.Model):
    class TipoServicio(models.TextChoices):
        SALON = "SALON", "Salón"
        LLEVAR = "LLEVAR", "Llevar"

    nombre = models.CharField(max_length=80)
    descripcion = models.TextField("descripción", blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tipo_servicio = models.CharField(
        "Tipo de Servicio",
        max_length=10,
        choices=TipoServicio.choices,
        default=TipoServicio.SALON,
    )
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        CategoriaPlato,
        on_delete=models.PROTECT,
        related_name="platos",
    )
    registrado_en = models.DateTimeField("registrado en", auto_now_add=True)

    class Meta:
        ordering = ["nombre", "pk"]

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_servicio_display()})"

    def get_absolute_url(self):
        return reverse("pedidos:Plato_detail", kwargs={"pk": self.pk})
