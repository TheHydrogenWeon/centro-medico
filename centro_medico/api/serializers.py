from rest_framework import serializers
from .models import Paciente
from .models import Especialidad
from .models import Doctor, Especialidad
from django.contrib.auth.models import User
from .models import FichaMedica, Paciente
from .models import Atencion, Doctor, FichaMedica
from .models import Medicamento
from .models import Examen

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'rut', 'nombre', 'fecha_nacimiento']


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'nombre']

class DoctorSerializer(serializers.ModelSerializer):
    especialidades = serializers.SlugRelatedField(
        many=True, slug_field='nombre', queryset=Especialidad.objects.all()
    )
    nombre_completo = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'nombre_completo', 'especialidades'] 

class FichaMedicaSerializer(serializers.ModelSerializer):
    paciente = serializers.StringRelatedField()  # Muestra el nombre del paciente

    class Meta:
        model = FichaMedica
        fields = ['id', 'paciente', 'fecha_creacion']        


class AtencionSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    ficha = serializers.PrimaryKeyRelatedField(queryset=FichaMedica.objects.all())

    class Meta:
        model = Atencion
        fields = ['id', 'ficha', 'doctor', 'fecha', 'anamnesis', 'diagnostico']

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['id', 'nombre']


class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = ['id', 'nombre']

from rest_framework import serializers
from .models import Especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

        