from django.shortcuts import render, redirect
from .models import Pessoa, Noticia
from .forms import PessoaForm, NoticiaForm
from .filters import FiltroPessoa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
# Create your views here.
def inicial(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	contexto = {
	'filtro': meufiltro
	}
	return render(request, 'home.html', contexto)

'''
noticias
'''

def noticias(request):
	return render(request, 'noticias/noticias.html')

def adminnoticias(request):
	noticias = Noticia.objects.all().order_by('-id')
	contexto = {
	'noticias': noticias
	}
	return render(request, 'noticias/adminnoticias.html', contexto)

def cadastronoticia(request):
	data_hora = datetime.now()
	form = NoticiaForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		noticia = form.save(commit=False)
		noticia.datahora = data_hora
		noticia.save()
		return redirect('adminnoticias')
	contexto = {
	'form': form
	}
	return render(request, 'noticias/cadastronoticia.html', contexto)
'''
Lista de colaboradores
'''
def listaramais(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	paginator = Paginator(meufiltro.qs, 12)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	contexto = {
	'filtro': meufiltro, 
	'contacts': contacts
	}
	return render(request, 'listaramais.html', contexto)

def adminramais(request):
	pessoa = Pessoa.objects.all().order_by('nome')
	meufiltro = FiltroPessoa(request.GET, queryset=pessoa)
	paginator = Paginator(meufiltro.qs, 10)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	contexto = {
	'filtro': meufiltro, 
	'contacts': contacts
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