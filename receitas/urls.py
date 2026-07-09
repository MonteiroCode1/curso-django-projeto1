from django.urls import path
from receitas import views


urlpatterns = [
    path('', views.Home), # é a raiz
    path('recipes/<int:id>/', views.recipes )
]