from django.urls import path
from .views import index, formulario_enviado, contacto, lista_usuarios, login_exitoso, nuevo_usuario, seccion_gatos, seccion_perros, lista_usuarios, nuevo_usuario
from .import views

urlpatterns = [

    path('', index, name="index"),
    path('', formulario_enviado, name="formulario-enviado"),
    path('', contacto, name="contacto"),
    path('', login_exitoso, name="login-exitoso"),
    path('', seccion_gatos, name="seccion-gatos"),
    path('', seccion_perros, name="seccion-perros"),
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
    path('nuevo_usuario', nuevo_usuario, name="nuevo_usuario"),

    #path('lista_usuarios', views.lista_usuarios),
    path('lista_usuarios', views.lista_usuarios, name="lista_usuarios"),
    path('nuevo_usuario', views.nuevo_usuario, name="nuevo_usuario"),

]