from django.db import models
import uuid


class Ingrediente(models.Model):
    id_ingrediente = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    ingrediente_name = models.CharField(
        max_length=50,
        blank=False,
        unique=True
    )

    ingrediente_cost = models.FloatField(
        blank=False
    )

    # class Meta:
    #     verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.ingrediente_name


class UnidadMedida(models.Model):
    id_unidad_medida = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    unidad_medida = models.CharField(
        max_length=50,
        blank=False,
        unique=True
    )

    # class Meta:
    #     verbose_name_plural = 'UnidadesMedidas'

    def __str__(self):
        return self.unidad_medida


class IngredienteExistencia(models.Model):
    id_ingrediente_existencia = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    ingrediente = models.ForeignKey(
        Ingrediente,
        on_delete=models.SET_NULL,
        null=True
    )

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        on_delete=models.SET_NULL,
        null=True
    )

    cantidad = models.FloatField(
        blank=False
    )

    # class Meta:
    #     verbose_name_plural = 'IngredientesExistencias'

    def __str__(self):
        return self.ingrediente.ingrediente_name


class IngredienteDetalle(models.Model):
    id_ingrediente_detalles = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    ingrediente = models.ForeignKey(
        Ingrediente,
        on_delete=models.SET_NULL,
        null=True
    )

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        on_delete=models.SET_NULL,
        null=True
    )

    cantidad = models.FloatField(
        blank=False
    )

    # class Meta:
    #     verbose_name_plural = 'IngredientesDetalles'

    def __str__(self):
        return self.ingrediente.ingrediente_name
