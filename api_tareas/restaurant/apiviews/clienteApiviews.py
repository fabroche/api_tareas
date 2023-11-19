from rest_framework import viewsets

# models
from restaurant.modelos.clientesModel import Cliente

# serializers
from restaurant.serializadores.clienteSerializer import ClienteSerializer


class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
