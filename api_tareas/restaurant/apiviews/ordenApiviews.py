from rest_framework import viewsets

# models
from restaurant.modelos.ordenesModel import Orden
from restaurant.modelos.ordenesModel import OrdenStatus
from restaurant.modelos.ordenesModel import OrdenDetalle

# serializers
from restaurant.serializadores.ordenSerializer import OrdenSerializer
from restaurant.serializadores.ordenSerializer import OrdenStatusSerializer
from restaurant.serializadores.ordenSerializer import OrdenDetalleSerializer


class OrdenView(viewsets.ModelViewSet):
    serializer_class = OrdenSerializer
    queryset = Orden.objects.all()


class OrdenStatusView(viewsets.ModelViewSet):
    serializer_class = OrdenStatusSerializer
    queryset = OrdenStatus.objects.all()


class OrdenDetalleView(viewsets.ModelViewSet):
    serializer_class = OrdenDetalleSerializer
    queryset = OrdenDetalle.objects.all()
