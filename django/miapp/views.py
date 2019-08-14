from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse( "<h1> Hola Mundo </h1>")
def cocina(request):
    return HttpResponse("<h1>¿Que haremos hoy?</h1>")
def gato(request):
    return HttpResponse("<h1>Miau</h1>")
def perro(request):
    return HttpResponse("<h1>Guau</h1>")
