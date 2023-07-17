from django.contrib import admin

# Register your models here.
from .models import Categoria, Noticia
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)