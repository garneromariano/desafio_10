from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    #Agrego personalizacion a mensaje de username
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=True,
        help_text='Requerido.  Letras, digitos y simbolos @/./+/-/_ .',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'max_length':'El nombre de Usuarion no puede tener mas de 150 caracteres'
        }

    )
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        required=True,
        error_messages={
            'required': 'Este campo es obligatorio.',
        }
    )
    password2 = forms.CharField(
        label='Conf Contraseña',
        widget=forms.PasswordInput,
        required=True,
        error_messages={
            'required': 'Este campo es obligatorio.',
        }
    )
    imagen = forms.ImageField( label='Imagen', required=False,
        help_text='Sube una imagen de perfil (opcional)'
        )
    
    facebook = forms.CharField(label='Facebook', required=False)
    whatsapp = forms.CharField(label='Numero-WhatsApp \n(Sin guiones)', required=False)
    instagram = forms.CharField(label='Instagram', required=False)   

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'imagen',
            'facebook', 
            'whatsapp',
            'instagram',
          
        ]
