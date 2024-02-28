from django import forms 

class ClienteForm(forms.Form):
    apellido = forms.CharField(max_length=50, required=True)
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    
class ComicForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    editorial = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(required=True)

class DistribuidorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    
class EnvioForm(forms.Form):
    empresa = forms.CharField(max_length=50, required=True)
    nombre = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)