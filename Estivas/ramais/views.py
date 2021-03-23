from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
# Create your views here.
def listaramais(request):
	pessoa = Pessoa.objects.all()
	contexto = {
	'lista_pessoa': pessoa
	}
	return render(request, 'listaramais.html', contexto)

def adminramais(request):
	pessoa = Pessoa.objects.all()
	contexto = {
	'lista_pessoa': pessoa
	}
	return render(request, 'adminramais.html', contexto)

def cadastroramal(request):
	form = PessoaForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('adminramais')
	contexto = {
	'formulario': form
	}
	return render(request, 'cadastro.html', contexto)

def atualizarramal(request, id):
	pessoa = Pessoa.objects.get(pk=id)
	form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)
	if form.is_valid():
		form.save()
		return redirect('adminramais')
	contexto = {
	'formulario': form
	}
	return render(request, 'cadastro.html', contexto)

def deletarramal(request,id):
	pessoa = Pessoa.objects.get(pk=id)
	pessoa.delete()
	return redirect('adminramais')