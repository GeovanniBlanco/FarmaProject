#se crean las vistas pero no los templates, esos son heredados
#el metodo render regresa la plantilla con el nombre del html, ya solo desde aqui ya queda ligado
#aca se puede acceder a los datos dentro de los modelos.

from django.shortcuts import render, HttpResponse ###se importa render para que muestre la pagina y la clase httpsResponse
from miFarma.models import Paciente #para el uso del modelo se debe importar de la aplicacion



def home (request):
    return render (request,"index.html")

# Create your views here.

def farmacia(request):
    return render(request,"farmacia.html")

def paciente(request):
    return render(request,'paciente.html')


#vista creada para guardar datos dentro del modelo, hay que crear la URL para que arroje el mensaje
def crear_paciente(request):
    cpaciente = Paciente(
        numPaciente = '3', #en cada ejemplo se agrega el valor de manera manual
        Nombre = 'Jose',
        apellidoP = '',
        apellidoM = 'Blanco',
        sexo = 'Masculino',
        direccion = 'Santiago Tepatlaxco',
        
    )

    cpaciente.save()
    
    return HttpResponse("Paciente creado: ")