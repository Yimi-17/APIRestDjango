from django.shortcuts import render
from rest_framework import viewsets
#from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from .serializers import TrabajadorSerializer
from .models import Trabajador
#from apirest import serializers



class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()        #queryset es una variable 
    serializer_class = TrabajadorSerializer

