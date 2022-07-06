from django.shortcuts import render
from Asistencial.models import cas, usuario, paciente, examen, archivo, bienAmbiente, bienImag, presAnemia,admiAnemia, exclusionAnemia, movimientoAnemia, bienPersonal, bienpat, dependencia, ambiente, personal, proveedor, provMaq, incidenciaDsi, maestro, bienHadware, bienSoftware, bienDetalleMonitor, nutricion, personalVpnAct, personalCertificado, valGlobalSub
from Asistencial.serializers import casSerializer ,usuarioSerializer, PacienteSerializer, ExamenSerializer, ArchivoSerializer, presAnemiaSerializer, admiAnemiaSerializer, exclusionAnemiaSerializer, movimientoAnemiaSerializer, bienAmbienteSerializer, bienImagSerializer, bienPersonalSerializer, bienpatSerializer, dependenciaSerializer, ambienteSerializer, personalSerializer, proveedorSerializer, provMaqSerializer, incidenciaDsiSerializer, maestroSerializer, bienHadwareSerializer, bienSoftwareSerializer, bienDetalleMonitorSerializer, nutricionSerializer, personalVpnActSerializer, personalCertificadoSerializer, valGlobalSubSerializer
from rest_framework import permissions, viewsets, filters

class casViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = cas.objects.all()
    serializer_class = casSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=tipoCas']


class usuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=usuario','=id']

# Create your views here.
class maestroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = maestro.objects.all()
    serializer_class = maestroSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

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
    queryset = examen.objects.all().order_by('-id')
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

class presAnemiaViewSet(viewsets.ModelViewSet):
    queryset = presAnemia.objects.all().order_by('-id')
    serializer_class = presAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id','=usuario__cas__codCas']

class admiAnemiaViewSet(viewsets.ModelViewSet):
    queryset = admiAnemia.objects.all().order_by('-id')
    serializer_class = admiAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=presAnemia__paciente__id','=usuario__cas__codCas']

class exclusionAnemiaViewSet(viewsets.ModelViewSet):
    queryset = exclusionAnemia.objects.all().order_by('-id')
    serializer_class = exclusionAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id','=usuario__cas__codCas']

class movimientoAnemiaViewSet(viewsets.ModelViewSet):
    queryset = movimientoAnemia.objects.all().order_by('-id')
    serializer_class = movimientoAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']

class nutricionViewSet(viewsets.ModelViewSet):
    queryset = nutricion.objects.all().order_by('-id')
    serializer_class = nutricionSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id','=usuario__cas__codCas','=pacNuevo']

class valGlobalSubViewSet(viewsets.ModelViewSet):
    queryset = valGlobalSub.objects.all().order_by('-id')
    serializer_class = valGlobalSubSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']


class bienpatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienpat.objects.all()
    serializer_class = bienpatSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['codEti']

class dependenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = dependencia.objects.all()
    serializer_class = dependenciaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['codDep']

class ambienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ambiente.objects.all()
    serializer_class = ambienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=dependencia__id']

class personalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = personal.objects.all()
    serializer_class = personalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=dniPer']

class bienImagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienImag.objects.all()
    serializer_class = bienImagSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class bienPersonalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienPersonal.objects.all()
    serializer_class = bienPersonalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class bienAmbienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienAmbiente.objects.all()
    serializer_class = bienAmbienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=bienpat__id']

class bienHadwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienHadware.objects.all()
    serializer_class = bienHadwareSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class bienSoftwareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienSoftware.objects.all()
    serializer_class = bienSoftwareSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class bienDetalleMonitorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = bienDetalleMonitor.objects.all()
    serializer_class = bienDetalleMonitorSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class proveedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = proveedor.objects.all()
    serializer_class = proveedorSerializer
    permission_classes = [permissions.IsAuthenticated]  
    filter_backends = [filters.SearchFilter]
    search_fields = ['=rucProveedor']

class provMaqViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = provMaq.objects.all()
    serializer_class = provMaqSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']

class incidenciaDsiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = incidenciaDsi.objects.all().order_by('-id')
    serializer_class = incidenciaDsiSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=personal__dniPer']

class personalVpnActViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = personalVpnAct.objects.all().order_by('-id')
    serializer_class = personalVpnActSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=personal__dniPer']

class personalCertificadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = personalCertificado.objects.all().order_by('-id')
    serializer_class = personalCertificadoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=personal__dniPer']