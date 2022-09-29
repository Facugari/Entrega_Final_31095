from mailbox import Maildir
from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, 'registro.html', {"usuarios" : usuarios})

def registrarmensaje(request):
    nombre = request.POST['txtnombre']
    mail = request.POST['txtmail']
    consulta = request.POST['txtconsulta']

    consulta = Usuario.objects.create (
        nombre = nombre, mail = mail, consulta = consulta
    )
    return redirect("/")


def edicionMensaje(request, nombre):
    usuario = Usuario.objects.get(nombre=nombre)
    return render(request, "edicionMensaje.html", {"usuario": usuario})


def editarMensaje(request):
    nombre = request.POST['txtnombre']
    mail = request.POST['txtmail']
    consulta = request.POST['txtconsulta']
    
    usuario = Usuario.objects.get(nombre=nombre)
    
    usuario.mail = mail
    usuario.consulta = consulta
    
    usuario.save()
    return redirect("/")

def eliminarmensaje(request, nombre):
    usuario = Usuario.objects.get(nombre=nombre)
    usuario.delete()
    return redirect("/")
