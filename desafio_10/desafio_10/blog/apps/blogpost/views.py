
import os
from django.conf import settings
from django.shortcuts import render,get_object_or_404, redirect

from .forms import ComentarioForm, PostForm,PostFormEdit
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django .http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# # Create your views here.
# def inicio (request,post_id):
#     post= Post.objects.all()
#     return render(request,'blogpost/inicio.html',{'post':post})


def inicio(request):
    contexto = {}
    post= Post.objects.all()
    titulo_busqueda = request.GET.get('busqueda_titulo')
    
    if titulo_busqueda:
        post = post.filter(titulo__icontains=titulo_busqueda)

    
    post = post.order_by('-fechaCreado')

    paginator = Paginator(post, 3)  

    page_number = request.GET.get('page')
    post_paginadas = paginator.get_page(page_number)

    contexto['posteos'] = post_paginadas    
    #print(post_paginadas[0])

    #print(post)

    return render(request, 'blogpost/inicio.html', contexto)

def detalle_post(request,pk):
    post = Post.objects.get(id=pk) # est es el nombre que asignamos en urls para el id

    comentarios = post.comentario.filter(activo =True)

    if request.method == 'POST':
        form = ComentarioForm (request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # ponemos false para que solo guarde cuando el usuario de click al boton enviar, si no se va guardar solo antes que presione guardar
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect("")
    else:
        form = ComentarioForm   

    return render(request,'blogpost/detalle_post.html',{'post':post,'comentarios':comentarios,'form':form})



# def detalle_Post(request, pk):
#     contexto = {}

#     n = Post.objects.get(pk=pk)
#     contexto['post'] = n

#     return render(request, 'blogpost/detalle_post.html', contexto)

@login_required
def crear_post(request):
    data = {
        'form': PostForm()
    }

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_image = form.cleaned_data.get('imagen') 
                     
           
            noticia = form.save(commit=False)
            noticia.imagen = new_image
            noticia.save()
            
            messages.success(request, 'Guardado correctamente')
            return redirect('blogpost:listar')
        else:
            data['form'] = form
            messages.error(request, 'No se pudo agregar. Verifica el formulario.')
      
    return render(request, 'blogpost/crear_post.html', data)

@login_required
def listar_post(request):
    
    post = Post.objects.all().order_by('-fechaCreado')
    print(post)
    paginator = Paginator(post, 10) 
    page_number = request.GET.get('page') 
    try:
       page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
         page_obj = paginator.get_page(1)
    except EmptyPage:
         page_obj = paginator.get_page(paginator.num_pages) 
     

    return render(request, 'blogpost/listar_post.html', {'page_obj': page_obj})

@login_required
def ver_post(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    return render(request, 'blogpost/ver_post.html', {'noticia': post})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(pk)
    data = {
        'form': PostFormEdit(instance=post)
        }

    if request.method == 'POST':
        form = PostFormEdit(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            new_image = form.cleaned_data.get('imagen1')  # Usa 'imagen1' o 'imagen2' según corresponda
            
            try:
                # Elimina la imagen anterior solo si se carga una nueva imagen
                if new_image:
                    ruta_foto = os.path.join(settings.MEDIA_ROOT, 'blogpost', str(post.imagen1))
                    if ruta_foto != os.path.join(settings.MEDIA_ROOT, 'blogpost', 'asd.jpg'):
                        os.remove(ruta_foto)
            except:
                pass
            
            post.imagen1 = new_image  # Usa 'imagen1' o 'imagen2' según corresponda
            form.save()
            
            messages.success(request, 'Guardado correctamente')
            return redirect('blogpost:listar')
        else:
             data['form'] = form
             messages.error(request, 'No se pudo guardar. Verifica el formulario.')
    else:
         form = data['form']  

    return render(request, 'blogpost/editar_post.html', data)


@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogpost:listar')
    return render(request, 'blogpost/eliminar_post.html', {'post': post})