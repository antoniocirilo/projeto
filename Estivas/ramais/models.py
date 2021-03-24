from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=150)
	setor = models.CharField('Setor', max_length=100)
	cargo = models.CharField('Cargo', max_length=50)
	matricula = models.CharField('Matricula', max_length=10)
	cc = models.CharField('Centro de custo', max_length=7, null=True)
	ramal = models.CharField('Ramal', max_length=4)
	foto = models.ImageField('Foto', upload_to='usuarios', default='usuarios/sem-foto.png')