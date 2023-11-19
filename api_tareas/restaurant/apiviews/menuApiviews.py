from rest_framework import viewsets

# models
from restaurant.modelos.menusModel import Menu
from restaurant.modelos.menusModel import MenuItem
from restaurant.modelos.menusModel import MenuItemCategory

# serializers
from restaurant.serializadores.menuSerializers import MenuSerializer
from restaurant.serializadores.menuSerializers import MenuItemSerializer
from restaurant.serializadores.menuSerializers import MenuItemCategorySerializer


class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class MenuItemView(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class MenuItemCategoryView(viewsets.ModelViewSet):
    serializer_class = MenuItemCategorySerializer
    queryset = MenuItemCategory.objects.all()
