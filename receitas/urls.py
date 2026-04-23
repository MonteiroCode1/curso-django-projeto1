from django.urls import path
from receitas.views import Home, Sobre, Contato


urlpatterns = [
    path('', Home), # é a raiz
    path('sobre/', Sobre),
    path('contato/', Contato)
]