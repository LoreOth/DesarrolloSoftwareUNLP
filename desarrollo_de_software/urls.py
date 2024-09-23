from django.contrib import admin
from django.urls import path, include
from formulario import views  # Importa tus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Agrega esta línea
    path('formulario/', include('formulario.urls')),  # http://127.0.0.1:8000/formulario/registrar-material/
]
