from django.shortcuts import render
from django.contrib import messages
from .models import Equipe, Postagem

from django.http import HttpResponse
from django.template import loader

from .forms import PostagemModelForm

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
	
def postagem(request):
		if str(request.method) == 'POST':
			form = PostagemModelForm(request.POST)
			if form.is_valid():
				
				form.save()

				messages.success(request, 'Postagem salva com sucesso.')
				form = PostagemModelForm()
			else:
				messages.error(request, 'Erro ao salvar postagem.')
		else:
			form = PostagemModelForm()
		context = {
			'form': form
		}
		return render(request, 'postagem.html', context)

	
def exibepost (request):

	verpost = Postagem.objects.all()
	context={
		'comentario': verpost,
	}
	return render(request, 'historias.html', context)
