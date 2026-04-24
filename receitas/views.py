from django.shortcuts import render # essa função renderiza arquivos
from django.http import HttpResponse

def Home(request):
    return render(request, 'receitas/home.html')

def Sobre(request):
    return HttpResponse('Sobre')

def Contato(request):
    return HttpResponse('Contato')