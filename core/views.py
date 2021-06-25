from django.shortcuts import render
from .models import Registrar
from .forms import UsuarioRegistrar

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def formulario_enviado(request):
    return render(request,'core/formulario_enviado.html')

def contacto(request):
    return render(request,'core/contacto.html')

def login_exitoso(request):
    return render(request,'core/login_exitoso.html')

def seccion_gatos(request):
    return render(request,'core/seccion_gatos.html')

def seccion_perros(request):
    return render(request,'core/seccion_perros.html')

def lista_usuarios(request):
    registrars = Registrar.objects.all() #obtiene todos los posteos 
    return render(request, 'core/lista_usuarios.html', {'registrars': registrars})

def nuevo_usuario(request):
    registrar = Registrar()

    if request.method == 'POST':
        nuevoRegistro = UsuarioRegistrar(request.POST, instance=registrar)
        nuevoRegistro.save()
        return render(request,'core/index.html')
    else:
        formulario = UsuarioRegistrar()
        return render(request, 'core/nuevo_usuario.html', {'formulario': formulario})