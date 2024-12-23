from rest_framework.routers import DefaultRouter
from .views import (
    PacienteViewSet, EspecialidadViewSet, DoctorViewSet,
    FichaMedicaViewSet, AtencionViewSet, MedicamentoViewSet,
    ExamenViewSet, formulario_pacientes
)
from django.urls import path

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'especialidades', EspecialidadViewSet, basename='especialidad')
router.register(r'doctores', DoctorViewSet, basename='doctor')
router.register(r'fichas', FichaMedicaViewSet, basename='ficha')
router.register(r'atenciones', AtencionViewSet, basename='atencion')
router.register(r'medicamentos', MedicamentoViewSet, basename='medicamento')
router.register(r'examenes', ExamenViewSet, basename='examen')

urlpatterns = router.urls + [
    path('pacientes/formulario/', formulario_pacientes, name='formulario_pacientes'),
]
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet
    