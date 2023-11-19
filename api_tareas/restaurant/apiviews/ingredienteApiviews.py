from rest_framework import viewsets

# models
from restaurant.modelos.ingredientesModel import UnidadMedida
from restaurant.modelos.ingredientesModel import Ingrediente
from restaurant.modelos.ingredientesModel import IngredienteDetalle
from restaurant.modelos.ingredientesModel import IngredienteExistencia

# serializers
from restaurant.serializadores.ingredienteSerializer import UnidadMedidaSerializer
from restaurant.serializadores.ingredienteSerializer import IngredienteSerializer
from restaurant.serializadores.ingredienteSerializer import IngredienteDetalleSerializer
from restaurant.serializadores.ingredienteSerializer import IngredienteExistenciaSerializer


class UnidadMedidaView(viewsets.ModelViewSet):
    serializer_class = UnidadMedidaSerializer
    queryset = UnidadMedida.objects.all()


class IngredienteView(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()


class IngredienteDetallesView(viewsets.ModelViewSet):
    serializer_class = IngredienteDetalleSerializer
    queryset = IngredienteDetalle.objects.all()


class IngredienteExistenciaView(viewsets.ModelViewSet):
    serializer_class = IngredienteExistenciaSerializer
    queryset = IngredienteExistencia.objects.all()
