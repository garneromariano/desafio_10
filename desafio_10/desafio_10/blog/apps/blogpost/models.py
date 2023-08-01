from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtituloGenral = models.CharField(max_length=255, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuerpo=models.TextField()
    slug = models.SlugField()
    fechaCreado= models.DateTimeField(auto_now_add=True, null=True) 
    titulo2 = models.CharField(max_length=255, null=True)
    subtituloGenral2 = models.CharField(max_length=255, null=True)
    cuerpo2 = models.TextField( null=True)
    imagen1 = models.ImageField(upload_to='blogpost/', null=True)
    imagen2 = models.ImageField(upload_to='blogpost/', null=True)
    pieDeFoto = models.CharField(max_length=255,null=True)
    pieDePosteo=models.TextField(null=True)
    #categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # def __str__(self):
    #      return  "post de " + ' | ' + self.autor +  ' | ' +  self.titulo
    def __str__(self):  # metodo  Tostring() 
     return self.titulo

class Comentario(models.Model):        
    usuario =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comentario')
    fechaCreado = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    activo=models.BooleanField(default=False)
    me_gusta= models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='comentario_Megusta')
    no_megusta=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='comentario_no_Megusta')
    def __str__(self):
        return "comentario de | {} | {}".format(self.usuario.username, self.contenido)
       # return f"comentario de {nombre} {contenido}"

User = get_user_model()

class MeGustaComentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.comentario}' 

   
