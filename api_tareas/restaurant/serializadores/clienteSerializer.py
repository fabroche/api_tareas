from rest_framework import serializers

from restaurant.modelos.clientesModel import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'