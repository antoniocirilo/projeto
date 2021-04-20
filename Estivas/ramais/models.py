from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=150)
	setor = models.CharField('Setor', max_length=100)
	cargo = models.CharField('Cargo', max_length=50)
	matricula = models.CharField('Matricula', max_length=6, unique=True)
	email = models.CharField('Email', null=True, max_length=50)
	cc = models.CharField('Centro de custo', max_length=7, null=True)
	ramal = models.CharField('Ramal', max_length=9, null=True, default='Sem ramal')
	foto = models.ImageField('Foto', upload_to='usuarios', default='usuarios/sem-foto.png')

class Noticia(models.Model):
	titulo = models.CharField('Título', max_length=50)
	subtitulo = models.CharField('subtítulo', max_length=50)
	noticia = models.TextField('Notícia')
	imagem = models.ImageField('Imagem', upload_to="fotoprincipal")
	anexo = models.FileField('Anexo:', upload_to='anexos', null = True)
	datahora = models.DateTimeField('datahora', null=True)

class Aniversariante(models.Model):
	#nome = models.CharField('Nome', max_length=150)
	#cargo = models.CharField('Cargo', max_length=50)
	padrao = models.ImageField('Foto', upload_to='aniversario')

class Informativo(models.Model):
	mes = models.CharField('Mes', max_length=15)
	fotoinformativo = models.ImageField('fotoinformativo', upload_to='informativo')
	anexo = models.FileField('Anexoinformativo', upload_to='informativo')