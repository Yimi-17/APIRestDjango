from rest_framework import serializers
from .models import Trabajador

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer): #clase
    class Meta:         #sobreescribir la clase
        model = Trabajador     
        fields = ['nombres', 'dni', 'celular', 'direccion', 'especialidad', 'email', 'area']    #campos a serializar 
