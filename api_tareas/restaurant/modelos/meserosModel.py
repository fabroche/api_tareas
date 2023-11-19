import uuid

from django.db import models


class Mesero(models.Model):
    id_mesero = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    nombre_mesero = models.CharField(
        max_length=50,
        blank=False
    )

    numero_telefono = models.CharField(
        max_length=8,
        null=True
    )

    def __str__(self):
        return self.nombre_mesero
