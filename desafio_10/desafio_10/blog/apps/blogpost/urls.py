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
]
    
