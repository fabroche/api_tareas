from rest_framework import serializers
from restaurant.modelos.menusModel import Menu
from restaurant.modelos.menusModel import MenuItem
from restaurant.modelos.menusModel import MenuItemCategory


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemCategory
        fields = '__all__'
