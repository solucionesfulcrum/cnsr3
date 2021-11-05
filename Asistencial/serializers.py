from django.contrib.auth.models import User, Group
from Asistencial.models import paciente, examen, archivo, bienAmbiente, bienPersonal, bienpat, dependencia, ambiente, personal, bienImag, proveedor, provMaq
from rest_framework import serializers

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'

class ExamenSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source = "paciente", read_only=True)
    class Meta:
        model = examen
        fields = '__all__'

class ArchivoSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source = "paciente", read_only=True)
    class Meta:
        model = archivo
        fields = '__all__'

class bienpatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienpat
        fields = '__all__'

class bienImagSerializer(serializers.HyperlinkedModelSerializer):
    datos_bienpat = bienpatSerializer(source = "bienpat", read_only=True)
    class Meta:
        model = bienImag
        fields = '__all__'

class dependenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dependencia
        fields = '__all__'

class ambienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ambiente
        fields = '__all__'  

class personalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = personal
        fields = '__all__'     

class bienPersonalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienPersonal
        fields = '__all__'    

class bienAmbienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienAmbiente
        fields = '__all__'         

class proveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = proveedor
        fields = '__all__'         

class provMaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = provMaq
        fields = '__all__' 