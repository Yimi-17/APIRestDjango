from django.db import models

# Create your models here.

class Trabajador(models.Model):

    nombres = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, null=True)
    celular = models.CharField(max_length=15, null=True)
    direccion = models.CharField(max_length=50, null=True)
    especialidad = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    area = models.CharField(max_length=50)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Trabajador")
        verbose_name_plural = ("Trabajadores")

    def __str__(self):
        return self.nombres

