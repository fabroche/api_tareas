from django.contrib import admin
# modelos
from restaurant.modelos.menusModel import Menu
from restaurant.modelos.menusModel import MenuItem
from restaurant.modelos.menusModel import MenuItemCategory
from restaurant.modelos.ingredientesModel import UnidadMedida
from restaurant.modelos.ingredientesModel import Ingrediente
from restaurant.modelos.ingredientesModel import IngredienteDetalle
from restaurant.modelos.ingredientesModel import IngredienteExistencia
from restaurant.modelos.mesasModel import Mesa
from restaurant.modelos.mesasModel import MesaStatus
from restaurant.modelos.mesasModel import MesaUbicacion
from restaurant.modelos.ordenesModel import Orden
from restaurant.modelos.ordenesModel import OrdenStatus
from restaurant.modelos.ordenesModel import OrdenDetalle
from restaurant.modelos.ventasModel import Venta
from restaurant.modelos.ventasModel import MetodoPago
from restaurant.modelos.ventasModel import MetodoPagoDetalle
from restaurant.modelos.meserosModel import Mesero
from restaurant.modelos.clientesModel import Cliente

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(UnidadMedida)
admin.site.register(Ingrediente)
admin.site.register(IngredienteDetalle)
admin.site.register(IngredienteExistencia)
admin.site.register(Mesa)
admin.site.register(MesaStatus)
admin.site.register(MesaUbicacion)
admin.site.register(Orden)
admin.site.register(OrdenStatus)
admin.site.register(OrdenDetalle)
admin.site.register(Venta)
admin.site.register(MetodoPago)
admin.site.register(MetodoPagoDetalle)
admin.site.register(Mesero)
admin.site.register(Cliente)
