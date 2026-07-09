from django.shortcuts import render # essa função renderiza arquivos

def Home(request):
    return render(request, 'receitas/page/home.html', context= {
        'nome': 'Guilherme'
    })

def recipes(request, id):
    return render(request, 'receitas/page/home.html', context= {
        'nome': 'Guilherme'
    })