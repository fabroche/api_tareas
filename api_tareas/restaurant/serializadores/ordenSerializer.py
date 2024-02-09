from rest_framework import serializers

from restaurant.modelos.clientesModel import Cliente
from restaurant.modelos.ordenesModel import Orden
from restaurant.modelos.ordenesModel import OrdenStatus
from restaurant.modelos.ordenesModel import OrdenDetalle
from restaurant.serializadores.clienteSerializer import ClienteSerializer
from restaurant.serializadores.menuSerializers import MenuItemSerializer
from restaurant.serializadores.mesaSerializer import MesaSerializer
from restaurant.serializadores.meseroSerializer import MeseroSerializer


class OrdenStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenStatus
        fields = '__all__'


class OrdenSerializer(serializers.ModelSerializer):
    orden_status = OrdenStatusSerializer(many=False)
    mesa = MesaSerializer(many=False)
    mesero = MeseroSerializer(many=True)
    cliente = ClienteSerializer(many=True)

    class Meta:
        model = Orden
        fields = '__all__'


class OrdenDetalleSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer(many=False)
    menu_item = MenuItemSerializer(many=False)

    class Meta:
        model = OrdenDetalle
        fields = '__all__'
