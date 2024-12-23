from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Paciente, Especialidad, Doctor, FichaMedica, Atencion, Medicamento, Examen
from .serializers import (
    PacienteSerializer,
    EspecialidadSerializer,
    DoctorSerializer,
    FichaMedicaSerializer,
    AtencionSerializer,
    MedicamentoSerializer,
    ExamenSerializer,
    
)
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rut', 'nombre']
    permission_classes = [AllowAny]



class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class FichaMedicaViewSet(ModelViewSet):
    queryset = FichaMedica.objects.all()
    serializer_class = FichaMedicaSerializer

class AtencionViewSet(ModelViewSet):
    queryset = Atencion.objects.all()
    serializer_class = AtencionSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class ExamenViewSet(ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

from django.shortcuts import render

def formulario_pacientes(request):
    return render(request, 'formulario_pacientes.html')


