from django.db import models

# Create your models here.

class paciente(models.Model):
    tipo_doc = models.CharField(max_length=40)
    num_doc = models.CharField(max_length=15)
    ape_pat = models.CharField(max_length=40)
    ape_mat = models.CharField(max_length=50)    
    nombres = models.CharField(max_length=50)
    fecha_nac = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True)
    estado = models.CharField(max_length=5, default=1)

    def __str__(self):
        return (self.nombres+' '+self.ape_pat+' '+self.ape_mat)

class examen(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, null=True)
    tipo_exam = models.CharField(max_length=50, null=True)
    archivo_exam = models.FileField(upload_to='media/', null=True)
    estado_lectura = models.CharField(max_length=30, null=True)
    estado = models.CharField(max_length=5, default='1')
    fecha_reg = models.DateTimeField(auto_now_add=True)
    user_reg = models.CharField(max_length=40, null=True)
    fecha_mod = models.DateTimeField(null=True)
    user_mod = models.CharField(max_length=50, null=True)
    fecha_eli = models.DateTimeField(null=True)
    user_eli = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tipo_exam