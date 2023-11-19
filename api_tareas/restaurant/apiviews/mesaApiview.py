from rest_framework import viewsets

# models
from restaurant.modelos.mesasModel import Mesa
from restaurant.modelos.mesasModel import MesaUbicacion
from restaurant.modelos.mesasModel import MesaStatus

# serializers
from restaurant.serializadores.mesaSerializer import MesaSerializer
from restaurant.serializadores.mesaSerializer import MesaUbicacionSerializer
from restaurant.serializadores.mesaSerializer import MesaStatusSerializer


class MesaView(viewsets.ModelViewSet):
    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()


class MesaUbicacionView(viewsets.ModelViewSet):
    serializer_class = MesaUbicacionSerializer
    queryset = MesaUbicacion.objects.all()


class MesaStatusView(viewsets.ModelViewSet):
    serializer_class = MesaStatusSerializer
    queryset = MesaStatus.objects.all()
