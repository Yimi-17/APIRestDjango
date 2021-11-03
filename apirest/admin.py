from django.contrib import admin
from .models import Trabajador

# Register your models here.

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'dni', 'celular', 'direccion', 'especialidad', 'email', 'area')

admin.site.register(Trabajador,TrabajadorAdmin)