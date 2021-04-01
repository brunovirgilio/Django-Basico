from django.shortcuts import render
from .models import Equipe

from django.http import HttpResponse
from django.template import loader

def index(request):
    exibeequipe = Equipe.objects.all()
    context={
        'equipe': exibeequipe,
    }
    return render(request, 'index.html', context)

def titulos(request,pk):
    vertitulos = Equipe.objects.get(id=pk)
    context={
        'titulo': vertitulos,
    }
    return render(request, 'titulos.html', context)

def postagem (request):
	    return render(request, 'postagem.html')
