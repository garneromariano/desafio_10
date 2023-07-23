from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from .models import Noticia, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm
from django.contrib import messages

import os
from django.conf import settings
from django.db.models import Q


# Create your views here.


#def inicio (request):
 #   return HttpResponse("<h1>Hola mundo</h1> <h2> desde django</h2>")

#def inicio (request):
#   return render(request, 'noticias/inicio.html')

#dataNotation c#
# decorador para ver las noticias solamente como usuario logueado

def inicio(request):
    contexto = {}
    id_categoria = request.GET.get('id')
    titulo_busqueda = request.GET.get('busqueda_titulo')
    print('id_categoria:', id_categoria)
    print('titulo_busqueda:', titulo_busqueda)
    
    noticias = Noticia.objects.all()  
    
    if id_categoria:
        noticias = noticias.filter(categoria_noticia=id_categoria)
    
    if titulo_busqueda:
        noticias = noticias.filter(Q(titulo__icontains=titulo_busqueda))
    
    noticias = noticias.order_by('-fecha')

    paginator = Paginator(noticias, 3)  
    page_number = request.GET.get('page')
    noticias_paginadas = paginator.get_page(page_number)

    categorias = Categoria.objects.all().order_by('nombre')

    contexto['noticias'] = noticias_paginadas
    contexto['categorias'] = categorias

    return render(request, 'noticias/inicio.html', contexto)


@login_required
def Detalle_Noticias(request, pk):
    contexto = {}

    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    return render(request, 'noticias/detalle.html', contexto)

@login_required
def crear_noticia(request):
    data = {
        'form': NoticiaForm()
    }

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_image = form.cleaned_data.get('imagen') 
                     
           
            noticia = form.save(commit=False)
            noticia.imagen = new_image
            noticia.save()
            
            messages.success(request, 'Guardado correctamente')
            return redirect('noticias:listar_noticias')
        else:
            data['form'] = form
            messages.error(request, 'No se pudo agregar. Verifica el formulario.')
      
    return render(request, 'noticias/crear_noticia.html', data)

@login_required
#def listar_noticias(request):
#    noticias = Noticia.objects.all()
#    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

def listar_noticias(request):
    categoria_seleccionada = request.GET.get('categoria')
    noticias = Noticia.objects.all().order_by('-fecha')
    

    if categoria_seleccionada:
        noticias = noticias.filter(categoria_noticia__id=categoria_seleccionada)
    
    paginator = Paginator(noticias, 10) 
    page_number = request.GET.get('page') 
    try:
       page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
         page_obj = paginator.get_page(1)
    except EmptyPage:
         page_obj = paginator.get_page(paginator.num_pages)

    
    categorias = Categoria.objects.all()    
     

    return render(request, 'noticias/listar_noticias.html', {'page_obj': page_obj, 'categorias': categorias})

@login_required
def ver_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)    
    return render(request, 'noticias/ver_noticia.html', {'noticia': noticia})

@login_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    
    data = {
        'form': NoticiaForm(instance=noticia)
    }
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        
        if form.is_valid():
            new_image = form.cleaned_data.get('imagen')  # Obtén la nueva imagen del formulario
            
            try:
                foto = request.FILES['imagen']
                ruta_foto = os.path.join(settings.MEDIA_ROOT, 'noticias', str(noticia.imagen))
                if ruta_foto != os.path.join(settings.MEDIA_ROOT, 'noticias', 'asd.jpg'):
                    os.remove(ruta_foto)
            except:
                pass
            
            noticia.imagen = new_image
            form.save()  # Guarda el formulario y la instancia de Noticia
            
            messages.success(request, 'Guardado correctamente')
            return redirect('noticias:listar_noticias')
        else:
            data['form'] = form
            messages.error(request, 'No se pudo guardar. Verifica el formulario.')
    else:
        form = data['form']  
    return render(request, 'noticias/editar_noticia.html', data)


@login_required
def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias:listar_noticias')
    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})