from django.db import models
from django.conf import settings
from tinymce import models as tinymce_models
from django.conf.urls.static import static


class Services(models.Model):
	title = models.TextField(max_length=60, verbose_name='Título',default='título')
	subtitle = models.TextField(default='A NMC Consultoria usa apenas informações atualizadas e novos métodos comerciais, fornecendo as soluções mais eficazes para o seu negócio', verbose_name='Subtitulo')
	text = tinymce_models.HTMLField(default='Texto')
	status = models.BooleanField(default=1,verbose_name='Publicado')
	date_create = models.DateTimeField(auto_now_add=True)
	date_alteration = models.DateTimeField(auto_now=True)
	image = models.ImageField(blank=True)
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
		

class Trainings(models.Model):
	title = models.TextField(max_length=60, verbose_name='Título',default='título')
	subtitle = models.TextField(default='A NMC Consultoria usa apenas informações atualizadas e novos métodos comerciais, fornecendo as soluções mais eficazes para o seu negócio', verbose_name='Subtitulo')
	text = tinymce_models.HTMLField(default='Texto')
	status = models.BooleanField(default=1,verbose_name='Publicado')
	date_create = models.DateTimeField(auto_now_add=True)
	date_alteration = models.DateTimeField(auto_now=True)

				
