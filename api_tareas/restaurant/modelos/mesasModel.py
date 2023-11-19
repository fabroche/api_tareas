from django.db import models
import uuid


class MesaUbicacion(models.Model):
    id_mesa_ubicacion = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    mesa_ubicacion = models.CharField(
        max_length=50,
        blank=False
    )

    def __str__(self):
        return self.mesa_ubicacion


class MesaStatus(models.Model):
    id_mesa_status = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    mesa_status = models.CharField(
        max_length=50,
        blank=False
    )

    def __str__(self):
        return self.mesa_status


class Mesa(models.Model):
    id_mesa = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    mesa_ubicacion = models.ForeignKey(
        MesaUbicacion,
        on_delete=models.SET_NULL,
        null=True
    )

    mesa_status = models.ForeignKey(
        MesaStatus,
        on_delete=models.SET_NULL,
        null=True
    )

    nombre_mesa = models.CharField(
        max_length=50,
        blank=False
    )

    def __str__(self):
        return self.nombre_mesa