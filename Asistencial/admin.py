from django.contrib import admin
from Asistencial.models import paciente, examen, archivo, bienAmbiente, bienPersonal, bienpat,dependencia,ambiente,personal, bienImag, proveedor, provMaq, maestro, incidenciaDsi
# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('tipo_doc','num_doc','ape_pat','ape_mat','nombres','fecha_nac','estado')

class examenAdmin(admin.ModelAdmin):
    list_display = ('paciente','tipo_exam','archivo_exam','estado_lectura','estado','fecha_reg','user_reg','fecha_mod','user_mod','fecha_eli','user_eli')
    search_fields = ('paciente__nombres', 'paciente__ape_pat', 'paciente__ape_mat',)

class archivoAdmin(admin.ModelAdmin):
    list_display = ('paciente','numHisCli','numBalda','estado','user_reg')
    search_fields = ('numHisCli',)

class imagenInline(admin.TabularInline):
    model = bienImag

class bienpatAdmin(admin.ModelAdmin):
    list_display = ('codEti','propBien','desBien','serBien','modBien','marBien','situBien','valBien','estBien')
    search_fields = ('codEti',)
    inlines = [imagenInline]

#Datos de inventario

class dependenciaAdmin(admin.ModelAdmin):
    list_display = ('codDep','descDep')
    search_fields = ('codDep',)

class ambienteAdmin(admin.ModelAdmin):
    list_display = ('codAmb','descAmb','dependencia')
    search_fields = ('codAmb',)

class personalAdmin(admin.ModelAdmin):
    list_display = ('dniPer','apePatPer','apeMatPer','nomPer','sexo','fecNacPer','codPlaPer','regPer','cargoPer','nivelPer','telefoPer','correoPer','direcPer','estPer','dependencia')
    search_fields = ('dniPer',)

class bienPersonalAdmin(admin.ModelAdmin):
    list_display = ('personal','bienpat')

class bienAmbienteAdmin(admin.ModelAdmin):
    list_display = ('ambiente','bienpat')

class proveedorAdmin(admin.ModelAdmin):
    list_display = ('rucProveedor','nombreProveedor','telefProveedor','direcProveedor','estadoProveedor')
    search_fields = ('rucProveedor',)

class provMaqAdmin(admin.ModelAdmin):
    list_display = ('usobien','bienpat')
    search_fields = ('usobien',)

class maestroAdmin(admin.ModelAdmin):
    list_display = ('codMaestro','descripMaestro','detalleMaestro')
    search_fields = ('codMaestro',)

class incidenciaDsiAdmin(admin.ModelAdmin):
    list_display = ('problema','clasiSolu','solucion','estado','userReg','fecha_reg','numTicket')
    search_fields = ('id',)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(examen, examenAdmin)
admin.site.register(archivo, archivoAdmin)

admin.site.register(personal, personalAdmin)
admin.site.register(bienpat, bienpatAdmin)
admin.site.register(dependencia, dependenciaAdmin)
admin.site.register(ambiente, ambienteAdmin)
admin.site.register(bienPersonal, bienPersonalAdmin)
admin.site.register(bienAmbiente, bienAmbienteAdmin)

admin.site.register(proveedor, proveedorAdmin)
admin.site.register(provMaq, provMaqAdmin)

admin.site.register(maestro, maestroAdmin)

admin.site.register(incidenciaDsi, incidenciaDsiAdmin)