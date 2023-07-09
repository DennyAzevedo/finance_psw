from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfil.models import Conta, Categoria
from django.contrib import messages
from django.contrib.messages import constants

def novo_valor(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all() 
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})