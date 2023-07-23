from django.urls import path
from . import views


app_name = 'blogpost'

# URL de app blogpost
urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('<int:post_id>/', views.post_detalle, name='post_detalle'),
    ]
