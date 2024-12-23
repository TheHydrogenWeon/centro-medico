from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def especialidades(request):
    return render(request, 'especialidades.html')

def doctores(request):
    return render(request, 'doctores.html')

def fichas(request):
    return render(request, 'fichas.html')

def atenciones(request):
    return render(request, 'atenciones.html')

def medicamentos(request):
    return render(request, 'medicamentos.html')

def examenes(request):
    return render(request, 'examenes.html')
