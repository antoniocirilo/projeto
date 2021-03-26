from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
from .filters import FiltroPessoa
# Create your views here.
def inicial(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	contexto = {
	'filtro': meufiltro
	}
	return render(request, 'home.html', contexto)
def listaramais(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	contexto = {
	'filtro': meufiltro
	}
	return render(request, 'listaramais.html', contexto)

def adminramais(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	contexto = {
	'filtro': meufiltro
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