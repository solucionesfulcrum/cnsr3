from django.contrib.auth.models import User, Group
from Asistencial.models import paciente, examen
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