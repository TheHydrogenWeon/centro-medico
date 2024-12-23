from django.contrib import admin
from django.urls import path, include
from .views import (
    index, pacientes, especialidades, doctores,
    fichas, atenciones, medicamentos, examenes
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Incluye las rutas de la API
    path('', index, name='index'),  # Página de inicio
    path('pacientes/', pacientes, name='pacientes'),
    path('especialidades/', especialidades, name='especialidades'),
    path('doctores/', doctores, name='doctores'),
    path('fichas/', fichas, name='fichas'),
    path('atenciones/', atenciones, name='atenciones'),
    path('medicamentos/', medicamentos, name='medicamentos'),
    path('examenes/', examenes, name='examenes'),
]
