from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
    
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)  
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)  
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
    
    
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)    
    