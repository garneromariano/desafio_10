from django.contrib import admin

# Register your models here.
from .models import Categoria, Noticia
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)

#@admin.register(Noticia)

#class NoticiaAdmin(admin.ModelAdmin):
    
#    ordering=('titulo')
#   search_fields=('titulo','fecha')
#admin.site.register(Noticia,NoticiaAdmin)
