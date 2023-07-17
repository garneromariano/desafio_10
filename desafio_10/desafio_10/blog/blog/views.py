from django.shortcuts import render, HttpResponse
from . import *
# Create your views here.

#def inicio (request):
  #  return render(request,'noticias/inicio.html')


def inicio1 (request):
    return render(request,'home1.html')

def inicio2 (request):
    return render(request,'home2.html')

def nosostros1(request) :
    return render(request,'nosotros2.html')

def nosostros2(request) :
    return render(request,'nosotros2.html')



