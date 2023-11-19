from rest_framework import serializers

from restaurant.modelos.ordenesModel import Orden
from restaurant.modelos.ordenesModel import OrdenStatus
from restaurant.modelos.ordenesModel import OrdenDetalle


class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'


class OrdenStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenStatus
        fields = '__all__'


class OrdenDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDetalle
        fields = '__all__'
