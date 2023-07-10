#se crean las vistas pero no los templates, esos son heredados
#el metodo render regresa la plantilla con el nombre del html, ya solo desde aqui ya queda ligado


from django.shortcuts import render, HttpResponse


def home (request):
    return render (request,"index.html")

# Create your views here.

def farmacia(request):
    return render(request,"farmacia.html")

def paciente(request):
    return render(request,'paciente.html')