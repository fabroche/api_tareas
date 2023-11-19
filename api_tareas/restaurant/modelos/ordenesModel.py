import uuid
from datetime import datetime

from django.db import models

from restaurant.modelos.clientesModel import Cliente
from restaurant.modelos.menusModel import MenuItem
from restaurant.modelos.mesasModel import Mesa
from restaurant.modelos.meserosModel import Mesero


class OrdenStatus(models.Model):
    id_orden_status = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    orden_status = models.CharField(
        max_length=50,
        blank=False
    )

    def __str__(self):
        return self.orden_status


class Orden(models.Model):
    id_orden = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    orden_status = models.ForeignKey(
        OrdenStatus,
        on_delete=models.SET_NULL,
        null=True
    )

    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.SET_NULL,
        null=True
    )

    fecha_orden = models.DateTimeField(
        blank=False,
        default=datetime.today
    )

    mesero = models.ManyToManyField(Mesero, blank=True)

    cliente = models.ManyToManyField(Cliente, blank=True)

    def __str__(self):
        return f'{self.mesa} / {self.fecha_orden}'


class OrdenDetalle(models.Model):
    id_orden_detalle = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE,
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        null=True
    )

    cantidad = models.IntegerField(
        blank=False
    )

    costo_menu_item_al_momento_de_la_venta = models.FloatField(
        blank=False
    )

    precio_menu_item_al_momento_de_la_venta = models.FloatField(
        blank=False
    )

    def __str__(self):
        return f'{self.cantidad} x {self.menu_item}'
