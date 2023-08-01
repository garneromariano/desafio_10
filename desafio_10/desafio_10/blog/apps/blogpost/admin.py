from django.contrib import admin
from .models import Post,Comentario,Categoria




class PostAdmin(admin.ModelAdmin):
    fields= ('titulo','subtituloGenral','slug','autor','cuerpo','titulo2','cuerpo2','imagen1','imagen2','pieDeFoto','pieDePosteo','subtituloGenral2','categoria' )

    prepopulated_fields={'slug':('titulo',)}
    


# Register your models here.
admin.site.register(Post,PostAdmin)

admin.site.register(Comentario)

admin.site.register(Categoria)