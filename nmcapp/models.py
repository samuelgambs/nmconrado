from django.db import models
from tinymce import models as tinymce_models


class Services(models.Model):
	title = models.TextField(max_length=60, verbose_name='Título',default='título')
	subtitle = models.TextField(default='A NMC Consultoria usa apenas informações atualizadas e novos métodos comerciais, fornecendo as soluções mais eficazes para o seu negócio', verbose_name='Subtitulo')
	text = tinymce_models.HTMLField(default='Texto')
	status = models.BooleanField(default=1,verbose_name='Publicado')
	date_create = models.DateTimeField(auto_now_add=True)
	date_alteration = models.DateTimeField(auto_now=True)

class Training(models.Model):
	title = models.TextField(max_length=60, verbose_name='Título',default='título')
	subtitle = models.TextField(default='A NMC Consultoria usa apenas informações atualizadas e novos métodos comerciais, fornecendo as soluções mais eficazes para o seu negócio', verbose_name='Subtitulo')
	text = tinymce_models.HTMLField(default='Texto')
	status = models.BooleanField(default=1,verbose_name='Publicado')
	date_create = models.DateTimeField(auto_now_add=True)
	date_alteration = models.DateTimeField(auto_now=True)

				

