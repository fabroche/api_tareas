from rest_framework import serializers

from restaurant.modelos.ingredientesModel import Ingrediente
from restaurant.modelos.ingredientesModel import IngredienteDetalle
from restaurant.modelos.ingredientesModel import IngredienteExistencia
from restaurant.modelos.ingredientesModel import UnidadMedida


class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class IngredienteDetalleSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(many=False)
    unidad_medida = UnidadMedidaSerializer(many=False)

    class Meta:
        model = IngredienteDetalle
        fields = '__all__'


class IngredienteExistenciaSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(many=False)
    unidad_medida = UnidadMedidaSerializer(many=False)

    class Meta:
        model = IngredienteExistencia
        fields = '__all__'
