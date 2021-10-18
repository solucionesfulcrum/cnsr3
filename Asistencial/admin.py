from django.contrib import admin
from Examenes_Escaneados.models import paciente, examen
# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('tipo_doc','num_doc','ape_pat','ape_mat','nombres','fecha_nac','estado')

class examenAdmin(admin.ModelAdmin):
    list_display = ('paciente','tipo_exam','archivo_exam','estado_lectura','estado','fecha_reg','user_reg','fecha_mod','user_mod','fecha_eli','user_eli')
    search_fields = ('paciente__nombres', 'paciente__ape_pat', 'paciente__ape_mat',)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(examen, examenAdmin)