from django import forms
from .models import Registrar

class UsuarioRegistrar(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = ('usuario', 'nombre', 'apellido', 'fecha_nacimiento', 'mail',)