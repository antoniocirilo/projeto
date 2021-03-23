from django.forms import ModelForm
from .models import Pessoa

class PessoaForm(ModelForm):
	class Meta:
		model = Pessoa
		fields = ['nome', 'setor', 'cargo', 'matricula', 'cc','ramal', 'foto']