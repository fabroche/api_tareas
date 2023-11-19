from rest_framework import viewsets

# models
from restaurant.modelos.meserosModel import Mesero

# serializers
from restaurant.serializadores.meseroSerializer import MeseroSerializer


class MeseroView(viewsets.ModelViewSet):
    serializer_class = MeseroSerializer
    queryset = Mesero.objects.all()
