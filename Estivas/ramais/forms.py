from django.forms import ModelForm
from .models import Pessoa
from django import forms

class PessoaForm(ModelForm):
	email = forms.CharField(required=False)
	class Meta:
		model = Pessoa
		fields = ['nome', 'setor', 'cargo', 'matricula', 'email', 'cc','ramal', 'foto']