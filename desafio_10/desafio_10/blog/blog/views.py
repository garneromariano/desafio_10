from django.shortcuts import render, HttpResponse
from . import *
from apps.blogpost.models import Post,User

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

#def inicio (request):
  #  return render(request,'noticias/inicio.html')


def inicio1 (request):
    return render(request,'home1.html')

def inicio2 (request):
    post = Post.objects.all()
        
    return render(request,'home2.html',{'post':post})

def nosostros1(request) :
    #return render(request,'nosotros2.html')
    pass

def nosostros2(request) :
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    return render(request,'nosotros2.html',context)


# redirect login
class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'  # Reemplaza por la plantilla que estés utilizando para el inicio de sesión
    success_url = reverse_lazy('inicio2')