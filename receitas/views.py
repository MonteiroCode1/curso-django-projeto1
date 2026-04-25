from django.shortcuts import render # essa função renderiza arquivos
from django.http import HttpResponse

def Home(request):
    return render(request, 'receitas/home.html', context= {
        'nome': 'Guilherme'
    })

def Sobre(request):
    return render(request, 'me_apague/temp.html')

def Contato(request):
    return HttpResponse('Contato')