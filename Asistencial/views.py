from django.shortcuts import render
from Asistencial.models import paciente, examen, archivo
from Asistencial.serializers import PacienteSerializer, ExamenSerializer, ArchivoSerializer
from rest_framework import permissions, viewsets, filters

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=num_doc']
    
class ExamenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo_exa']

class ArchivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = archivo.objects.all().order_by('-id')
    serializer_class = ArchivoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']