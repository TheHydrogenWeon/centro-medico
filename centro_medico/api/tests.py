from rest_framework.routers import DefaultRouter
from .views import (
    PacienteViewSet, EspecialidadViewSet, DoctorViewSet,
    FichaMedicaViewSet, AtencionViewSet, MedicamentoViewSet, ExamenViewSet
)

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'doctores', DoctorViewSet)
router.register(r'fichas', FichaMedicaViewSet)
router.register(r'atenciones', AtencionViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'examenes', ExamenViewSet)

urlpatterns = router.urls

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
