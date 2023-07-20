from django.db import models

# Create your models here.

#se crean los modelos para los datos de las tablas (entidades), faltan agregar las entidades correspondientes

class Paciente(models.Model):
    numPaciente = models.TextField()
    Nombre = models.TextField()
    apellidoP = models.TextField()
    apellidoM = models.TextField()
    sexo = models.TextField()
    direccion = models.TextField()
 


class Medicamento(models.Model):
    nombre = models.TextField()
    lote = models.TextField()
    presentacion = models.TextField()
    codBarras = models.TextField()
    laboratorio = models.TextField()

#cambio realizado
    

