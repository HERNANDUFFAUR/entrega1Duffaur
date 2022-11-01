from contextvars import Context
import datetime
from re import template
from string import Template
from xmlrpc.client import DateTime
from django.http import HttpResponse  
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.models import Persona
from home.forms import PersonaFomulario, BusquedaPersonaFomulario

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'la fecha y hora actual es {fecha_y_hora}')

def ver_personas(request):
    personas = Persona.objects.all()         
   
    return render(request, 'home/ver_personas.html', {'personas': personas})

def busqueda_personas(request):
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = None     
    
    formulario = BusquedaPersonaFomulario()
    
    return render(request, 'home/busqueda_personas.html', {'personas':personas, 'formulario':formulario})
        

def crear_persona(request):
    
    if request.method == 'POST':
        formulario = PersonaFomulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_alta= data['fecha_alta']
            
            if not fecha_alta:
               fecha_alta = datetime.now()
                 
            persona = Persona(nombre=nombre, 
                            apellido=apellido, 
                            edad=edad,
                            fecha_alta=fecha_alta)
            persona.save()
        
        # DIRECCIONA A URL DE VER PERSONAS
        return redirect('ver_personas')
    formulario = PersonaFomulario()
    
    return render(request,'home/crear_personas.html',{'formulario': formulario})

def index(request):
    return render(request,'home/index.html')

