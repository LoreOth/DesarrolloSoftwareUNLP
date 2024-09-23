# formulario/urls.py
from django.urls import path
from .views import registrar_material

urlpatterns = [
    path('registrar-material/', registrar_material, name='registrar_material'),
]
