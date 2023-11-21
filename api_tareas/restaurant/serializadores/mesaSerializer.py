from rest_framework import serializers

from restaurant.modelos.mesasModel import Mesa
from restaurant.modelos.mesasModel import MesaStatus
from restaurant.modelos.mesasModel import MesaUbicacion


class MesaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaStatus
        fields = '__all__'


class MesaUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaUbicacion
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    mesa_ubicacion = MesaUbicacionSerializer(many=False)
    mesa_status = MesaStatusSerializer(many=False)

    class Meta:
        model = Mesa
        # fields = ['id_mesa', 'nombre_mesa', 'mesa_ubicacion', 'mesa_status']
        fields = '__all__'
