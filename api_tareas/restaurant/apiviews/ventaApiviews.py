from rest_framework import viewsets

# models
from restaurant.modelos.ventasModel import Venta
from restaurant.modelos.ventasModel import MetodoPago
from restaurant.modelos.ventasModel import MetodoPagoDetalle

# serializers
from restaurant.serializadores.ventaSerializer import VentaSerializer
from restaurant.serializadores.ventaSerializer import MetodoPagoSerializer
from restaurant.serializadores.ventaSerializer import MetodoPagoDetalleSerializer


class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()


class MetodoPagoView(viewsets.ModelViewSet):
    serializer_class = MetodoPagoSerializer
    queryset = MetodoPago.objects.all()


class MetodoPagoDetalleView(viewsets.ModelViewSet):
    serializer_class = MetodoPagoDetalleSerializer
    queryset = MetodoPagoDetalle.objects.all()
