from django import forms
from .models import Noticia
from datetime import date

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = "__all__"
        widgets = {
        "fecha": forms.SelectDateWidget()
         }    
    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].initial = date.today()