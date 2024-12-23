from django.db import models

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django
    especialidades = models.ManyToManyField(Especialidad)

    def __str__(self):
        return self.user.get_full_name()  # Nombre completo del usuario

class FichaMedica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ficha de {self.paciente.nombre}"

class Atencion(models.Model):
    ficha = models.ForeignKey(FichaMedica, related_name='atenciones', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    anamnesis = models.TextField()
    diagnostico = models.TextField()

    def __str__(self):
        return f"Atención del {self.fecha} por {self.doctor}"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Examen(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

