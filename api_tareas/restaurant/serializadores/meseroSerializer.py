from rest_framework import serializers

from restaurant.modelos.meserosModel import Mesero


class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = '__all__'
