
import os
from django.conf import settings
from django.shortcuts import render,get_object_or_404, redirect

from .forms import ComentarioForm, PostForm,PostFormEdit,CategoriasForm
from .models import Post,Comentario,MeGustaComentario,Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django .http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib import messages

from django.http import JsonResponse

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

def detalle_post2(request,pk):
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


def detalle_post3(request, pk):
    post = Post.objects.get(id=pk) # Este es el nombre que asignamos en urls para el id
    comentarios = post.comentario.filter(activo=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False) # Ponemos False para que solo guarde cuando el usuario haga clic al botón enviar
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect(reverse('blogpost:detalle', args=[pk]))
    else:
        form = ComentarioForm()

    # Si el usuario no está autenticado, hacemos el formulario como Vacio
    if not request.user.is_authenticated:
        form = None

    return render(request, 'blogpost/detalle_post.html', {'post': post, 'comentarios': comentarios, 'form': form})

# def detalle_Post(request, pk):
#     contexto = {}

#     n = Post.objects.get(pk=pk)
#     contexto['post'] = n

#     return render(request, 'blogpost/detalle_post.html', contexto)
def detalle_post2(request, pk):
    post = Post.objects.get(id=pk)  # Este es el nombre que asignamos en urls para el id
    comentarios = post.comentario.filter(activo=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post

            # Verificamos si el usuario está autenticado antes de asignarle el comentario
            if request.user.is_authenticated:
                new_form.usuario = request.user

            new_form.save()
            return HttpResponseRedirect(reverse('blogpost:detalle', args=[pk]))
    else:
        form = ComentarioForm()

    
    if request.user.is_authenticated:
        user_comentarios = comentarios.filter(usuario=request.user)
    else:
        user_comentarios = None

    return render(request, 'blogpost/detalle_post.html', {'post': post, 'comentarios': comentarios, 'form': form, 'user_comentarios': user_comentarios})
    
def detalle_post(request, pk):
  
    post = Post.objects.get(id=pk)
    comentarios = post.comentario.filter(activo=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post

            if request.user.is_authenticated:
                new_form.usuario = request.user  # Establecer el usuario del comentario

            new_form.save()
            return HttpResponseRedirect(reverse('blogpost:detalle', args=[pk]))
    else:
        form = ComentarioForm()

    if request.user.is_authenticated:
        user_comentarios = comentarios.filter(usuario=request.user)
    else:
        user_comentarios = None

    return render(request, 'blogpost/detalle_post.html', {'post': post, 'comentarios': comentarios, 'form': form, 'user_comentarios': user_comentarios})

@login_required
@user_passes_test(lambda user: user.is_staff)
def crear_post(request):
   if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.imagen1 = form.cleaned_data.get('imagen1')
            post.imagen2 = form.cleaned_data.get('imagen2')

            post.save()
            messages.success(request, 'Guardado correctamente')
            return redirect('blogpost:listar')
        else:
            messages.error(request, 'No se pudo agregar. Verifica el formulario.')
   else:
        form = PostForm()

   data = {'form': form}
    
   return render(request, 'blogpost/crear_post.html', data)

@login_required
@user_passes_test(lambda user: user.is_staff)
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
@user_passes_test(lambda user: user.is_staff)
def ver_post(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    return render(request, 'blogpost/ver_post.html', {'noticia': post})

@login_required
@user_passes_test(lambda user: user.is_staff)
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(pk)
    data = {
        'form': PostFormEdit(instance=post)
        }

    if request.method == 'POST':
        form = PostFormEdit(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            new_image1 = form.cleaned_data.get('imagen1')  
            new_image2 = form.cleaned_data.get('imagen2')  
            try:
                # Elimina la imagen anterior solo si se carga una nueva imagen
                if new_image1:
                    ruta_foto1= os.path.join(settings.MEDIA_ROOT, 'blogpost', str(post.imagen1))
                    if ruta_foto1 != os.path.join(settings.MEDIA_ROOT, 'blogpost', 'default.jpg'):
                        os.remove(ruta_foto1)
                if new_image2:
                    ruta_foto2 = os.path.join(settings.MEDIA_ROOT, 'blogpost', str(post.imagen2))
                    if ruta_foto2 != os.path.join(settings.MEDIA_ROOT, 'blogpost', 'default.jpg'):
                        os.remove(ruta_foto2)        
            except:
                pass
            
            post.imagen1 = new_image1
            post.imagen2 = new_image2
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
@user_passes_test(lambda user: user.is_staff)
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blogpost:listar')
    return render(request, 'blogpost/eliminar_post.html', {'post': post})


@login_required
def editarComentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
        
    if not request.user.is_authenticated or request.user != comentario.usuario:
        return redirect('blogpost:detalle', pk=comentario.post.pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('blogpost:detalle', pk=comentario.post.pk)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'blogpost/editar_comentario.html', {'form': form})


def megustaComentario(request, pk):

    print(pk)
    action = request.POST.get('action', None)
    print(action)
    if request.method == 'POST' and request.user.is_authenticated:
        comentario = get_object_or_404(Comentario, pk=pk)
        action = request.POST.get('action', None)

        if action == 'like':
            comentario.me_gusta.add(request.user)
            comentario.no_megusta.remove(request.user)
        elif action == 'unlike':
            comentario.me_gusta.remove(request.user)
            comentario.no_megusta.remove(request.user)
        elif action == 'dislike':
            comentario.no_megusta.add(request.user)
            comentario.me_gusta.remove(request.user)
        elif action == 'undislike':
            comentario.no_megusta.remove(request.user)
            comentario.me_gusta.remove(request.user)

        return JsonResponse({
            'likes': comentario.me_gusta.count(),
            'dislikes': comentario.no_megusta.count(),
        })
    else:
        return JsonResponse({'error': 'No se pudo procesar el me gusta.'}, status=400)
    


# seccion categorias para Blog
@login_required
@user_passes_test(lambda user: user.is_staff)
def categoria_listar(request):
    categorias = Categoria.objects.all()
    return render(request, 'blogpost/categorias_Blog/listar_categoria.html', {'categorias': categorias})

@login_required
@user_passes_test(lambda user: user.is_staff)
def categoria_detalle(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    print(categoria)
    return render(request, 'blogpost/categorias_Blog/detalle_categoria.html', {'categoria': categoria})

@login_required
@user_passes_test(lambda user: user.is_staff)
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost:categoria_listar')
    else:
        form = CategoriasForm()
    return render(request, 'blogpost/categorias_Blog/crear_editar_categoria.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_staff)
def categoria_Editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriasForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('blogpost:categoria_listar')
    else:
        form = CategoriasForm(instance=categoria)
    return render(request, 'blogpost/categorias_Blog/crear_editar_categoria.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_staff)
def categoria_Eliminar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_listar')
    return render(request, 'blogpost/categorias_Blog/categoria_confirm_delete.html', {'categoria': categoria})    
