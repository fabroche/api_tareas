from rest_framework import serializers

from restaurant.modelos.ventasModel import Venta
from restaurant.modelos.ventasModel import MetodoPago
from restaurant.modelos.ventasModel import MetodoPagoDetalle
from restaurant.serializadores.ordenSerializer import OrdenSerializer


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class MetodoPagoDetalleSerializer(serializers.ModelSerializer):
    metodo_pago = MetodoPagoSerializer(many=False)

    class Meta:
        model = MetodoPagoDetalle
        fields = '__all__'


class VentaSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer(many=False)
    metodo_pago = MetodoPagoSerializer(many=True)

    class Meta:
        model = Venta
        fields = '__all__'
