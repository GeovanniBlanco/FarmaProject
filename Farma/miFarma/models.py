from django.db import models

# Create your models here.

#se crean los modelos para los datos de las tablas (entidades), faltan agregar las entidades correspondientes

class Paciente(models.Model):
    numPaciente = models.TextField()
    Nombre = models.TextField()
    apellidoP = models.TextField()
    apellidoM = models.TextField()
    fechaNac = models.DateField
    edad = models.IntegerField
    sexo = models.TextField()
    direccion = models.TextField()
    telefono = models.IntegerField


class Medicamento(models.Model):
    nombre = models.TextField()
    caducidad = models.DateField
    lote = models.TextField()
    cantidad = models.IntegerField
    presentacion = models.TextField()
    codBarras = models.TextField()
    laboratorio = models.TextField()

#cambio realizado
    

