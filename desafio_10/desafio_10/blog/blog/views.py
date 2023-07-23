from django.shortcuts import render, HttpResponse
from . import *
from apps.blogspot.models import Post
# Create your views here.

#def inicio (request):
  #  return render(request,'noticias/inicio.html')


def inicio1 (request):
    return render(request,'home1.html')

def inicio2 (request):
    post = Post.objects.all()
        
    return render(request,'home2.html',{'post':post})

def nosostros1(request) :
    return render(request,'nosotros2.html')

def nosostros2(request) :
    return render(request,'nosotros2.html')



