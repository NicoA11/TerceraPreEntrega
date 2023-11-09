
from django.urls import path
from .views import formulario_insertar

urlpatterns = [
    path('formulario_insertar/', formulario_insertar, name='formulario_insertar'),
    # Otras URL...
]

