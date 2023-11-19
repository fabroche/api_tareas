import uuid

from django.db import models
from django.contrib.auth.models import User


class Cliente(User):
    id_cliente = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    nombre_cliente = models.CharField(
        max_length=50,
        blank=False
    )

    numero_telefono = models.CharField(
        max_length=8,
        null=True
    )

    def __str__(self):
        return self.username
