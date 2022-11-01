from django import forms

class PersonaFomulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_alta = forms.DateField(required=False,input_formats=['%Y/%m/%d'])

class BusquedaPersonaFomulario (forms.Form):
    nombre = forms.CharField(max_length=30, required=False)

        