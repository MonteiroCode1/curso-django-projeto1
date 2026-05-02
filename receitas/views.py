from django.shortcuts import render # essa função renderiza arquivos

def Home(request):
    return render(request, 'page/home.html', context= {
        'nome': 'Guilherme'
    })