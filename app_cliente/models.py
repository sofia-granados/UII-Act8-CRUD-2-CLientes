from django.db import models

# Create your models here.
class Cliente(models.Model):
    apepaterno = models.CharField(max_length=50)
    apematerno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    alergias = models.TextField(blank=True, null=True)    
    def __str__(self):
        return f'CLiente:{self.apepaterno} {self.apematerno} {self.nombre} {self.domicilio} {self.email}{self.telefono} {self.alergias}'