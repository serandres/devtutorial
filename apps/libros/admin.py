from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'resumen', 'imagen_portadas')
	list_filter = ('autor',)
	search_fields = ('nombre', 'autor__nombre')

	def imagen_portadas(self,libro):
		url = libro.traer_url_portadas()
		tag = "<img src='%s'>" % url
		return tag

	imagen_portadas.allow_tags = True

# Register your models 
admin.site.register(Libro,LibroAdmin)