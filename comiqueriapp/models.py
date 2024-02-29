from django.db import models
from django.contrib.auth.models import User

# Clases
    
class Comic(models.Model):
    nombre = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.editorial}, {self.autor}"

    
    
class Cliente(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    
    class Meta:
        ordering = ["apellido"]
        
    def __str__(self):
        return f"{self.apellido} {self.nombre}, {self.telefono}"

    
    
class Distribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    
    class Meta:
        verbose_name = "Distribuidor"
        verbose_name_plural = "Distribuidores"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.telefono}"
    
    
    
class Envio(models.Model):
    empresa = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    
    class Meta:
        ordering = ["empresa"]

    def __str__(self):
        return f"{self.empresa} {self.nombre}, {self.telefono}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.imagen}"    
    