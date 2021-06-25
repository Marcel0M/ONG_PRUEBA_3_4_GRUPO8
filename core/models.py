from django.db import models
from django.utils import timezone

# Create your models here.

class Registrar(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(blank=True)
    mail = models.CharField(max_length=100)
    
    def publish(self):
        #self.published_date = timezone.now()
        self.save()
        
    def _str_(self):
        return self.usuario     


