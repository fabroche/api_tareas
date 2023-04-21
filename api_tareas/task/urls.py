from .apiviews import TaskView
from django.urls import path, include
from rest_framework import routers

# para Swagger
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# Routing
router = routers.DefaultRouter()
router.register(r'tasks', TaskView)

# Swagger Docs
swaggerUi_schema = get_schema_view(
    title='SwaggerUi ApiTask',
    description='Guide for the API Task',
    version='v1.0.0',
)

urlpatterns = [
    path('api/v1/', include(router.urls)),

    # End Point para construir el schema de configuracion del Swagger
    path('schema/', swaggerUi_schema, name="schema-apiTask"),

    # End Point para visitar la Documentacion de la Api
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'schema-apiTask'}
    ), name='swagger-ui'),
]
