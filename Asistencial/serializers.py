from django.contrib.auth.models import User, Group
from Asistencial.models import paciente, examen, archivo, presAnemia, admiAnemia, exclusionAnemia, movimientoAnemia, bienAmbiente, bienPersonal, bienpat, dependencia, ambiente, personal, bienImag, proveedor, provMaq, maestro, incidenciaDsi, bienHadware
from rest_framework import serializers

class maestroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = maestro
        fields = '__all__' 

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
        
#Clinicas Anemia

class presAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source="paciente", read_only=True)    
    class Meta:
        model = presAnemia
        fields = '__all__'

class admiAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPres = presAnemiaSerializer(source="presAnemia", read_only=True)    
    class Meta:
        model = admiAnemia
        fields = '__all__'

class exclusionAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source="paciente", read_only=True)   
    class Meta:
        model = exclusionAnemia
        fields = '__all__'

class movimientoAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source="paciente", read_only=True)   
    class Meta:
        model = movimientoAnemia
        fields = '__all__'

#Inventario

class dependenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dependencia
        fields = '__all__'

class ambienteSerializer(serializers.HyperlinkedModelSerializer):
    datosDependencia = dependenciaSerializer(source = "dependencia", read_only=True)
    class Meta:
        model = ambiente
        fields = '__all__'  

class personalSerializer(serializers.HyperlinkedModelSerializer):
    datosDependencia = dependenciaSerializer(source = "dependencia", read_only=True)
    class Meta:
        model = personal
        fields = '__all__'     

class bienPersonalSerializer(serializers.HyperlinkedModelSerializer):
    datos_bienpat = bienpatSerializer(source = "bienpat", read_only=True)
    datosPersonal = personalSerializer(source = "personal", read_only=True)
    class Meta:
        model = bienPersonal
        fields = '__all__'    

class bienAmbienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienAmbiente
        fields = '__all__'        

class bienHadwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bienHadware
        fields = '__all__'     

class proveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = proveedor
        fields = '__all__'         

class provMaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = provMaq
        fields = '__all__' 

class incidenciaDsiSerializer(serializers.HyperlinkedModelSerializer):
    datosPersonal = personalSerializer(source = "personal", read_only=True)
    datosEstado = maestroSerializer(source = "estado", read_only=True)
    class Meta:
        model = incidenciaDsi
        fields = '__all__' 