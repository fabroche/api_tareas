import uuid

from django.db import models

from restaurant.modelos.ordenesModel import Orden


class MetodoPago(models.Model):
    id_metodo_pago = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    metodo_pago = models.CharField(
        max_length=50,
        blank=False
    )

    def __str__(self):
        return self.metodo_pago


class MetodoPagoDetalle(models.Model):
    id_metodo_pago_detalle = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    metodo_pago = models.ForeignKey(
        MetodoPago,
        on_delete=models.CASCADE
    )

    monto = models.FloatField(
        blank=False
    )

    def __str__(self):
        return self.metodo_pago


class Venta(models.Model):
    id_venta = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    orden = models.OneToOneField(
        Orden,
        on_delete=models.DO_NOTHING,
    )

    metodo_pago = models.ManyToManyField(
        MetodoPagoDetalle
    )

    fecha_venta = models.DateTimeField(
        blank=False
    )

    importe_total = models.FloatField(
        blank=False
    )

    salario_del_dia = models.FloatField(
        blank=False
    )

    inversion_total = models.FloatField(
        blank=False
    )

    ganancia_bar = models.FloatField(
        blank=False
    )

    ganancia_alianza = models.FloatField(
        blank=False
    )

    def __str__(self):
        return self.fecha_venta
