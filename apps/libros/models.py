from django.db import models
from apps.autores.models import Autor
from django.conf import settings

# Create your models here.
class Libro(models.Model):
	autor = models.ManyToManyField(Autor)
	nombre = models.CharField(max_length=50)
	resumen = models.TextField(max_length=300)
	portada = models.ImageField(upload_to = 'portadas')

	def __unicode__(self):
		return self.nombre

	def traer_url_portadas(self):
		return settings.MEDIA_ROOT+'/'+str(self.portada)
