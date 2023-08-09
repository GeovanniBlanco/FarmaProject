#se crean las vistas pero no los templates, esos son heredados
#el metodo render regresa la plantilla con el nombre del html, ya solo desde aqui ya queda ligado
#aca se puede acceder a los datos dentro de los modelos.

from django.shortcuts import render, HttpResponse ###se importa render para que muestre la pagina y la clase httpsResponse
from requests import *
from miFarma.models import Paciente #para el uso del modelo se debe importar de la aplicacion
from miFarma.models import usuarios


def home (request):
    return render (request,"index.html")

# Create your views here.

def farmacia(request):
    return render(request,"farmacia.html")


######--------------------URL pacientes----------------------######
def paciente(request):

### Mostrando todos los pacientes 
    pacientes = Paciente.objects.all() #el metodo "all" nos traera todos los datos de la base
    
    return render(request, "paciente.html", { 
        'pacientes': pacientes
    })


#___________________________________________________________________________________________________________________#
#vista creada para guardar datos dentro del modelo, hay que crear la URL para que arroje el mensaje


def crear_paciente(request):

    if request.method == 'GET':
        
        numPaciente = request.GET['numPaciente']
        Nombre = request.GET['Nombre']
        apellidoP = request.GET['apellidoP']
        apellidoM = request.GET['apellidoM']
        sexo = request.GET['sexo']
        direccion = request.GET['direccion']

        cpaciente = Paciente(
            numPaciente = numPaciente, #en cada ejemplo se agrega el valor de manera manual
            Nombre = Nombre, #en cada ejemplo se agrega el valor de manera manual
            apellidoP = apellidoP, #en cada ejemplo se agrega el valor de manera manual
            apellidoM = apellidoM, #en cada ejemplo se agrega el valor de manera manual
            sexo = sexo, #en cada ejemplo se agrega el valor de manera manual
            direccion = direccion, #en cada ejemplo se agrega el valor de manera manual
        )
        cpaciente.save()
    
        return HttpResponse(f"Paciente creado: {cpaciente.Nombre} - {cpaciente.apellidoP}")
    else:
        return HttpResponse("<h2> No se guardo el paciente</h2>")
    

    

#_____________________________________________________________________________________________________________________#

### Traer un valor de la tabla de la base de datos ###
def ver_paciente(request): #se define la vista para mostrar los valores consultados
    
    #el bloque try y except son para la excepcion, en caso de que no encuentre el valor
    try: 
        verPaciente = Paciente.objects.get(id=2)  #esta variable hara la busqueda, si encuentra el valor regresa la linea de abajo, si no, pasa a la excepcion dentro del reponse
        response = f"Paciente: {verPaciente.Nombre}"
    except: 
        response = "<h1> Paciente no encontrado"

    return HttpResponse(response)

#______________________________________________________________________________________________________________________#
#### se actualiza por medio de la URL, es importante poner el ID en la URL 

def actualizar_paciente(request, id):
    
    #bloque try para confirmar si esta o no el paciente
    try: 
        paciente = Paciente.objects.get(pk=id) # hace la consulta para el valor que se va a actualizar
    
        paciente.Nombre = "Jose" #actualizacion del campo nombre dentro de la entidad
        paciente.apellidoP = "Blanco" #actualizacion del campo nombre dentro de la entidad
        paciente.apellidoM = "De La Cruz" #actualizacion del campo nombre dentro de la entidad
        response = f"Paciente: {paciente.Nombre}, {paciente.apellidoP}" #resultado obtenido (imprime la pantalla)
        paciente.save() #metodo save para guardar lo que esta dentro de la variable paciente
    except:
        response = "No se actualizo paciente por que no se encontro"

    return HttpResponse(response)
#________________________________________________________________________________________________________________________#
### creacion de usuario

def usuario(request):
    usuario = usuarios(
        usuario = 'geovanni', #en cada ejemplo se agrega el valor de manera manual
        contraseña = '1234', #en cada ejemplo se agrega el valor de manera manual
        rol = 'admin', #en cada ejemplo se agrega el valor de manera manual
        )

    usuario.save()
    
    return HttpResponse(f"Usuario creado: {usuario.usuario} - {usuario.rol}")



   




