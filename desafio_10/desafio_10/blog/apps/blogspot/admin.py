from django.contrib import admin
from .models import Post




class PostAdmin(admin.ModelAdmin):
    fields= ('titulo','slug','autor','cuerpo' )

    prepopulated_fields={'slug':('titulo',)}



# Register your models here.
admin.site.register(Post,PostAdmin)