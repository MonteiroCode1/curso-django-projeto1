from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse('Home 1')

def Sobre(request):
    return HttpResponse('Sobre')

def Contato(request):
    return HttpResponse('Contato')