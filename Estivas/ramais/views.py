from django.shortcuts import render

# Create your views here.
def listaramais(request):
	return render(request, 'listaramais.html')