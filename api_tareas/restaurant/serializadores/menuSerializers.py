from rest_framework import serializers

from restaurant.modelos.ingredientesModel import IngredienteDetalle
from restaurant.modelos.menusModel import Menu
from restaurant.modelos.menusModel import MenuItem
from restaurant.modelos.menusModel import MenuItemCategory
from restaurant.serializadores.ingredienteSerializer import IngredienteDetalleSerializer


class MenuItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemCategory
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    menu_item_category = MenuItemCategorySerializer(many=False)
    ingredientes = IngredienteDetalleSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'
