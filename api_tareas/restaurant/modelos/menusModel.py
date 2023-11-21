from django.db import models
import uuid

from restaurant.modelos.ingredientesModel import IngredienteDetalle


class Menu(models.Model):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    menu_name = models.CharField(
        max_length=50,
        blank=False,
        unique=True
    )

    menu_item = models.ManyToManyField(
        'MenuItem',
        blank=True,
        help_text='Seleccione los elementos del menu'
    )

    # class Meta:
    #     verbose_name_plural = 'Menus'

    def __str__(self):
        return self.menu_name


class MenuItemCategory(models.Model):
    id_menu_item_category = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    menu_item_category = models.CharField(
        max_length=50,
        blank=False,
    )

    # class Meta:
    #     verbose_name_plural = 'MenuItemCategorys'

    def __str__(self):
        return self.menu_item_category


class MenuItem(models.Model):
    id_menu_item = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4
    )

    menu_item_category = models.ForeignKey(
        MenuItemCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    menu_item_name = models.CharField(
        max_length=50,
        blank=False
    )

    menu_item_cost = models.FloatField(
        blank=False
    )

    menu_item_price = models.FloatField(
        blank=False
    )

    ingredientes = models.ManyToManyField(IngredienteDetalle, blank=True)

    # class Meta:
    #     verbose_name_plural = 'MenuItems'

    def __str__(self):
        return self.menu_item_name
