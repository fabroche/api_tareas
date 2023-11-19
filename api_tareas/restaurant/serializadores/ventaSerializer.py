from rest_framework import serializers

from restaurant.modelos.ventasModel import Venta
from restaurant.modelos.ventasModel import MetodoPago
from restaurant.modelos.ventasModel import MetodoPagoDetalle


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class MetodoPagoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPagoDetalle
        fields = '__all__'
