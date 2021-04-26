from django.forms import ModelForm
from .models import Pessoa, Noticia, Aniversariante, Informativo
from django import forms

class PessoaForm(ModelForm):
	email = forms.CharField(required=False)
	class Meta:
		model = Pessoa
		fields = ['nome', 'setor', 'cargo', 'matricula', 'email', 'cc','ramal', 'foto']

class NoticiaForm(ModelForm):
	anexo = forms.FileField(required=False)
	class Meta:
		model = Noticia
		fields = ['titulo', 'subtitulo', 'noticia', 'imagem', 'anexo']

class AniversarianteForm(ModelForm):
	class Meta:
		model = Aniversariante
		fields = ['padrao']

class InformativoForm(ModelForm):
	class Meta:
		model = Informativo
		fields = ['mes', 'fotoinformativo', 'anexo']