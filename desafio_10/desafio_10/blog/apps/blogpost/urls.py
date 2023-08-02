from django.urls import path
from . import views


app_name = 'blogpost'

# URL de app blogpost
urlpatterns = [
    path('',views.inicio,name='inicio'),    
    path('crear/', views.crear_post, name='crear'),
    path('detalle/<int:pk>/', views.detalle_post, name='detalle'),   
    path('editar/<int:pk>/',views.editar_post,name='editar'),
    path('eliminar/<int:pk>/',views.eliminar_post,name='eliminar'),
    path('listar/',views.listar_post,name='listar'),
    path('editarComentario/<int:pk>/',views.editarComentario,name='editarComentario'),
    path('megustaComentario/<int:pk>/', views.megustaComentario, name='megustaComentario'),
    #Seccion Categorias oara el Blog
    path('categorias/', views.categoria_listar, name='categoria_listar'),
    path('categorias/<int:pk>/', views.categoria_detalle, name='categoria_detalle'),
    path('categorias/create/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:pk>/update/', views.categoria_Editar, name='categoria_Editar'),
    path('categorias/<int:pk>/delete/', views.categoria_Eliminar, name='categoria_Eliminar'),
]
    
