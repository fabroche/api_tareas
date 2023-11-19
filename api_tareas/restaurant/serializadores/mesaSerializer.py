from rest_framework import serializers

from restaurant.modelos.mesasModel import Mesa
from restaurant.modelos.mesasModel import MesaStatus
from restaurant.modelos.mesasModel import MesaUbicacion


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'


class MesaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaStatus
        fields = '__all__'


class MesaUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesaUbicacion
        fields = '__all__'
