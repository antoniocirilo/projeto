import django_filters
from .models import Pessoa
from django.db import models

class FiltroPessoa(django_filters.FilterSet):
	class Meta:
		model = Pessoa
		fields = ['nome', 'setor']
		filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             }
         }