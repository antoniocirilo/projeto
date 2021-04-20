from django.shortcuts import render, redirect
from .models import Pessoa, Noticia, Aniversariante, Informativo
from .forms import PessoaForm, NoticiaForm, AniversarianteForm, InformativoForm
from .filters import FiltroPessoa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
# Create your views here.
def home(request):
	noticia1 = Noticia.objects.all().order_by('-id')[:3]
	aniversariantes = Aniversariante.objects.all()
	informativo = Informativo.objects.all().order_by('-id')[:1]
	contexto = {
	'noticias': noticia1,
	'aniversariantes': aniversariantes,
	'informativo': informativo
	}
	return render(request, 'index.html', contexto)
'''
noticias
'''

def noticias(request):
	noticias = Noticia.objects.all().order_by('-id')
	paginator = Paginator(noticias, 10)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	contexto = {
	'noticias': noticias,
	'contacts': contacts
	}
	return render(request, 'noticias/noticias.html', contexto)

def noticiaespecifica(request, id):
	noticia = Noticia.objects.get(pk=id)
	contexto = {
	'noticia': noticia
	}
	return render(request, 'noticias/noticia.html', contexto)

def adminnoticias(request):
	noticias = Noticia.objects.all().order_by('-id')
	paginator = Paginator(noticias, 10)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	contexto = {
	'noticias': noticias,
	'contacts': contacts
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

def atualizarnoticia(request, id):
	data_hora = datetime.now()
	noticia = Noticia.objects.get(pk=id)
	form = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
	if form.is_valid():
		noticia = form.save(commit=False)
		noticia.datahora = data_hora
		noticia.save()
		return redirect('adminnoticias')
	contexto = {
	'form': form
	}
	return render(request, 'noticias/cadastronoticia.html', contexto)

def deletarnoticia(request, id):
	noticia = Noticia.objects.get(pk=id)
	noticia.delete()
	return redirect('adminnoticias')

'''
aniversariantes
'''
def aniversariantes(request):
	aniversariante = Aniversariante.objects.all()
	contexto = {
	'aniversariantes': aniversariante
	}
	return render(request, 'aniveriantes/aniversariantes.html', contexto)

def cadastroaniversariantes(request):
	form = AniversarianteForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('aniversariantes')
	contexto = {
	'form': form
	}
	return render(request, 'aniveriantes/cadastroaniversariantes.html', contexto)

def atualizaraniversariantes(request, id):
	aniversariante = Aniversariante.objects.get(pk=id)
	form = AniversarianteForm(request.POST or None, request.FILES or None, instance=aniversariante)
	if form.is_valid():
		form.save()
		return redirect('aniversariantes')
	contexto = {
	'form': form
	}
	return render(request, 'aniveriantes/cadastroaniversariantes.html', contexto)

def deletaraniversariantes(request,id):
	aniversariante = Aniversariante.objects.get(pk=id)
	aniversariante.delete()
	return redirect('aniversariantes')

'''
Informativo
'''
def informativo(request):
	informativo = Informativo.objects.all()
	contexto = {
	'informativo': informativo
	}
	return render(request, 'informativo/informativo.html', contexto)

def cadastroinformativo(request):
	form = InformativoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('informativo')
	contexto = {
	'form': form
	}
	return render(request, 'informativo/cadastroinformativo.html', contexto)

def atualizarinformativo(request, id):
	informativo = Informativo.objects.get(pk=id)
	form = InformativoForm(request.POST or None, request.FILES or None, instance=informativo)
	if form.is_valid():
		form.save()
		return redirect('informativo')
	contexto = {
	'form': form
	}
	return render(request, 'informativo/cadastroinformativo.html', contexto)

def infoespecifico(request, mes):
	informativo = Informativo.objects.get(mes=mes)
	contexto = {
	'informativo': informativo
	}
	return render(request, 'informativo/infoespecifico.html', contexto)
'''
Lista de colaboradores
'''
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