from django.shortcuts import render

# formulario/views.py
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .form import MaterialForm

BONITA_API_URL = 'http://localhost:8080/bonita/API/bpm/process/'
BONITA_LOGIN_URL = 'http://localhost:8080/bonita/loginservice'
BONITA_USER = 'admin'
BONITA_PASSWORD = 'bpm'

def iniciar_instancia_bonita(process_id, variables, bonita_session):
    headers = {
        'X-Bonita-API-Token': bonita_session.cookies['X-Bonita-API-Token'],
        'Content-Type': 'application/json'
    }
    data = {
        "processDefinitionId": process_id,
        "variables": variables
    }
    response = requests.post(f"{BONITA_API_URL}instantiation", json=data, headers=headers)
    return response.json()

def registrar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.cleaned_data['material']
            cantidad = form.cleaned_data['cantidad']
            
            # Autenticación en Bonita
            login_data = {
                'username': BONITA_USER,
                'password': BONITA_PASSWORD,
                'redirect': False
            }
            bonita_session = requests.post(BONITA_LOGIN_URL, data=login_data)
            
            # Variables para enviar a Bonita
            variables = [
                {"name": "material", "value": material},
                {"name": "cantidad", "value": str(cantidad)}
            ]
            
            # Iniciar el proceso en Bonita
            process_id = "ID_DEL_PROCESO_EN_BONITA"  # Reemplaza con el ID real del proceso
            response = iniciar_instancia_bonita(process_id, variables, bonita_session)
            
            return JsonResponse(response)
    else:
        form = MaterialForm()
    
    return render(request, 'registrar_material.html', {'form': form})

def home(request):
    return render(request, 'home.html') 
