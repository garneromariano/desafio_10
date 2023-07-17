from django.urls import path
from . import views

app_name = 'contactos'

# URL de app noticias
urlpatterns = [
    path('',views.contacto,name='contacto')
    ]
